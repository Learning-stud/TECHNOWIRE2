from django.db import models


class blogs(models.Model):
 title = models.CharField(max_length=100)
 content= models.models.TextField()
dateAZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ_publish = models.DateTimeField(auto_now_add=True)

 def  __str__(self):
  return self.title