from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Todo)
admin.site.register(Event)
admin.site.register(Timer)
admin.site.register(Note)
admin.site.register(Photo)

