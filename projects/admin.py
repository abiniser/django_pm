from django.contrib import admin
from . import models
# Register your models here.
# this for adding things into the admin page
admin.site.register(models.category)
admin.site.register(models.projects)
admin.site.register(models.task)

