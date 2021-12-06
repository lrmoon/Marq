from django.contrib import admin
from .models import Todo, Event

# Register your models here.
admin.site.register(Todo)
admin.site.register(Event)