from django.db import models

class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

