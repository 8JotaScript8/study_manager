from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

import subjects
from .models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['name']
    template_name = 'subjects/subject_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)