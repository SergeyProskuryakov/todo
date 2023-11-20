from django.contrib import admin
from .models import Tasks
from .models import Categories


# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Tasks._meta.fields if field.name != 'id'
    ]
admin.site.register(Tasks, TasksAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Categories._meta.fields if field.name != 'id'
    ]
admin.site.register(Categories, CategoriesAdmin)