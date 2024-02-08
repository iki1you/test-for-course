from app.internal.models.admin_user import AdminUser
from django.db import models
from django.forms import forms


class Profile(models.Model):
    phone = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.phone
