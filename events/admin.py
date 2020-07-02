from django.contrib import admin
from .models import Event
from tinymce.widgets import TinyMCE
from django.db import models

class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Event, EventAdmin)