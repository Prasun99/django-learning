from django.db import models

class student(models.Model):
  name = models.CharField()
  age = models.IntegerField()
  email = models.EmailField(unique=True)
def __str__(self):
  return self.name