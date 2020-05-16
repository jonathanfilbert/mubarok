from django.db import models
import uuid


# Create your models here.


class Pesan(models.Model):
    nama = models.TextField()
    secret = models.CharField(default=uuid.uuid4(),unique=True,max_length=36)
    story = models.TextField()
    img = models.TextField()