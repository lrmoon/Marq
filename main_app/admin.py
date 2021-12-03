from django.contrib import admin
from .models import Todo, Importance_levels, Event

# Register your models here.
admin.site.register(Todo)
admin.site.register(Importance_levels)
admin.site.register(Event)