from django.contrib import admin
from .models import Tasks

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Tasks._meta.fields if field.name != 'id'
    ]
admin.site.register(Tasks, TasksAdmin)