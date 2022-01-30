from django.db import models


# Create your models here.
class Document(models.Model):
    documentId = models.AutoField(primary_key=True)
    category = models.CharField(max_length=25)
    creator = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    file_name = models.CharField(max_length=200)


def set_creator(self, creator):
    self.creator = creator
