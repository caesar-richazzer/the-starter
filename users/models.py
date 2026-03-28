from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 1. USER FIRST
class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# 2. PROFILE SECOND
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default='default.png', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    tagline = models.CharField(max_length=100, blank=True)