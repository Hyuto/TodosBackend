from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'complete', 'user']
    list_filter = ['user']
    search_fields = ['user']
    ordering = ['user', 'deadline']


admin.site.register(Todo, TodoAdmin)
