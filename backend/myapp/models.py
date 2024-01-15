from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_campus_ambassador = models.BooleanField(default=False)
    referral_code = models.CharField(max_length=10, blank=True, null=True)

class Referral(models.Model):
    code = models.CharField(max_length=10, unique=True)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
