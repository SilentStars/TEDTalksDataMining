from django.db import models
from django.contrib.auth.models import AbstractUser

class Movie(models.Model):
    name = models.CharField(max_length= 200)
    url = models.CharField(max_length= 300)
    tag = models.CharField(max_length= 200)

    def __str__(self):
        return self.url


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    tag = models.CharField(max_length=100,blank=True)
    class Meta(AbstractUser.Meta):
        pass
