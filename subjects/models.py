from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()

class Subject(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    def __str__(self):
        return self.name