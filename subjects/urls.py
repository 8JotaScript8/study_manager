from django.urls import path
from .views import SubjectCreateView, SubjectListView

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),   
    path('create/', SubjectCreateView.as_view(), name='subject_create'),
]