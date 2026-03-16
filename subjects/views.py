from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

import subjects
from .models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['name']
    template_name = 'subjects/subject_form.html'
    success_url = reverse_lazy('subjects:subject_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url
        

        return super().get_success_url()
    

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)


class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'subjects/subject_confirm_delete.html'
    success_url = reverse_lazy('subjects:subject_list')

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)