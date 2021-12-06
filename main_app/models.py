from django.db import models
from datetime import date
from django.urls import reverse

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=400)
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
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Note(models.Model):
  title = models.CharField(max_length=100)
  note = models.TextField(max_length=500)
  


class Photo(models.Model):
  url = models.CharField(max_length=250)
  note = models.OneToOneField(Note, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for note_id: {self.note_id} @{self.url}"