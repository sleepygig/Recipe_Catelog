from django.db import models

# Create your models here.
class Students(models.Model):
    #id =models.AutoField()
    name =models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField(null=True , blank=True)
    image=models.ImageField()
    file=models.FileField()

class Car(models.Model):
    car_name=models.TextField(max_length=100)
    speed=models.IntegerField(default=50)
    
    
    def __str__(self):
        return self.car_name
    