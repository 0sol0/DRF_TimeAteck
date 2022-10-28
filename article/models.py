from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODE, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    