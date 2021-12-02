from django.db import models
from datetime import date
from django.urls import reverse

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Importance_levels(models.Model):
    name = models.CharField(max_length=250)
    abreviation = models.CharField(max_length=1)


class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=400)
    date = models.DateField('Due Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    IMPORTANCE = [
        ('Important', 'Important'),
        ('General', 'General'),
        ('Minor', 'Minor')
    ]
    importance = models.CharField(
        max_length=20,
        choices=IMPORTANCE,
        default=IMPORTANCE[1][0]
    )

    def __str__(self):
      return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()