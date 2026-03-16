from django.urls import path
from .views import SubjectCreateView, SubjectDeleteView, SubjectListView

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),   
    path('create/', SubjectCreateView.as_view(), name='subject_create'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
]
