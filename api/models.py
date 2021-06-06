from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=10, unique=True)
    subscription_level = models.IntegerField(null=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)