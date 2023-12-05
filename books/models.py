from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    favorites = models.ManyToManyField('Book', related_name='favorites', blank=True)
    cart = models.ManyToManyField('Book', related_name='shopping_cart', blank=True)
    #pass

class Book(models.Model):

    #user = models.ForeignKey(User, on_delete=models.CASCADE)# dont think this is needed
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='images/listings', blank=True)
    #image = models.URLField(default='')


    def __str__(self):
        return f'{self.title} for {self.price}'
    
#comments?