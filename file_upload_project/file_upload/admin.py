from django.contrib import admin

from .models import File


@admin.register(File)
class File(admin.ModelAdmin):

    list_display = ("file", "uploaded_at", "processed")
