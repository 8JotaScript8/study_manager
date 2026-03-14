from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone

from .models import Task
from .forms import TaskForm
from subjects.models import Subject

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task = Task.objects.filter(user=self.request.user)

        total_tasks = task.count()
        completed_tasks = task.filter(completed=True).count()
        pending_tasks = task.filter(completed=False).count()
        late_tasks = task.filter(
            completed=False,
            due_date__lt=timezone.now().date()
        ).count()

        progress = 0
        if total_tasks > 0:
            progress = int((completed_tasks / total_tasks) * 100)

        context.update({
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'late_tasks': late_tasks,
            'progress': progress
        })


        return context
    


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(
            user=self.request.user
        ).select_related('subject')

        status = self.request.GET.get('status')
        subject = self.request.GET.get('subject')

        if status == 'completed':
            queryset = queryset.filter(completed=True)

        elif status == 'pending':
            queryset = queryset.filter(completed=False)

        elif status == 'late':
            queryset = queryset.filter(
                completed=False,
                due_date__lt=timezone.now().date()
            )

        if subject:
            queryset = queryset.filter(subject_id=subject)

        return queryset.order_by('due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = context['tasks']

        context['pending_tasks'] = tasks.filter(completed=False)
        context['completed_tasks'] = tasks.filter(completed=True)

        context['atrasadas'] = tasks.filter(
            completed=False,
            due_date__lt=timezone.now().date()
        )

        context['subjects'] = Subject.objects.filter(user=self.request.user)

        context['current_status'] = self.request.GET.get('status', '')
        context['current_subject'] = self.request.GET.get('subject', '')

        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        print("FORM VALID")
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("FORM INVALID:", form.errors)
        return super().form_invalid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class ToggleTaskCompleteView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['completed']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        return redirect('tasks:list')
    

from django.shortcuts import render, redirect
from .forms import SignUpForm


def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')


@login_required
def uncomplete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = False
    task.save()
    return redirect('task_list')
