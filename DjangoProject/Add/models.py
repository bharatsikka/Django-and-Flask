from django.db import models
from datetime import datetime
# Create your models here.

class Add(models.Model):
    first = models.FloatField()
    second = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now, blank= True)
    def __str__(self):
        return self.title

