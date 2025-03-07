from django.db import models
 

#This is where you will make the table
class Item(models.Model):
 name = models.CharField(max_length=255)
 description = models.TextField(blank=True)
 price = models.DecimalField(max_digits=10, decimal_places=2)

 def __str__(self):
  return self.name
