from django.contrib import admin
from .models import Employee, Task

admin.site.register(Employee)
# Register your models here.
admin.site.register(Task)