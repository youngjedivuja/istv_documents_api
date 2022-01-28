from django.db import models


# Create your models here.
class Document(models.Model):
    documentId = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    creatorId = models.IntegerField()
    owner = models.CharField(max_length=20)
    ownerId = models.IntegerField()
    roles = models.CharField(max_length=200)
