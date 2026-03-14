from core.models import BaseModel
from django.db import models
from subjects.models import Subject
from django.contrib.auth.models import User
from django.utils import timezone

class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        return self.title

    
    @property
    def is_late(self):
        if self.due_date and not self.completed:
            return self.due_date < timezone.now().date()
        return False