from django.db import models

# Create your models here.

class Book(models.Model):
     title=models.CharField(max_length=70)
     price=models.IntegerField()
    
     def str(self):
        return self.title