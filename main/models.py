from typing import Text
from django.db import models

# Create your models here.

class ToDo(models.Model):
    Text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)