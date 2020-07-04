from django.contrib import admin
from .models import Workshop
from tinymce.widgets import TinyMCE
from django.db import models


class WorkshopAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Workshop, WorkshopAdmin)