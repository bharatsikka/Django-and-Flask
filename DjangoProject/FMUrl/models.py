from django.db import models

# Create your models here.
class URL(models.Model):
    provider_url = models.URLField()
