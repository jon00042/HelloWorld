from django.db import models
from apps.travel_app.models import User

class Bill(models.Model):
    desc = models.CharField(max_length=128)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ####################################################
    user = models.ForeignKey(User, related_name='bills', on_delete=True)

