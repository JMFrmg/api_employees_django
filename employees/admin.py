from django.contrib import admin
from employees import models

admin.site.register(models.Department)
admin.site.register(models.Employee)
