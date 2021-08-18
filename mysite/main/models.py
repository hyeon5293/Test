from django.db import models

class Post(models.Model):
    furniture_Name = models.CharField(max_length=100)
    furniture_Link = models.URLField()
    sale_Percentage = models.CharField(max_length=10)
    current_Price = models.CharField(max_length=20)
    previous_Price = models.CharField(max_length=20)
    furniture_Img = models.URLField()
    
    def __str__(self):
        return self.furniture_Name
# Create your models here.