from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.short_url

