from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length= 200)
    url = models.CharField(max_length= 300)
    tag = models.CharField(max_length= 200)

    def __str__(self):
        return self.url