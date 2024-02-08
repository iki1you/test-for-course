from django import forms
from django.contrib import admin
from .models import Profile
from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
