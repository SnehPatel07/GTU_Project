from django.contrib import admin
from . import models
# Register your models here.

class Admin_list(admin.ModelAdmin):
    list_display = ['username', 'email', 'contact']

admin.site.register(models.Admin_User,Admin_list)