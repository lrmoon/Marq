from django.db import models
from datetime import date
from django.urls import reverse

IMPORTANCE = (
  ('I', 'Important'),
  ('G', 'General'),
  ('M', 'Minor')
)

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=10)
  description = models.CharField(max_length=400)

  date = models.DateField('Due Date')
  importance = models.CharField(
      max_length=1,
      choices=IMPORTANCE,
      default=IMPORTANCE[0][1]
  )

  def __str__(self):
    return self.title
      
