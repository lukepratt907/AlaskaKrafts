from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    favorites = models.ManyToManyField('Book', related_name='favorites', blank=True)
    cart = models.ManyToManyField('Book', related_name='shopping_cart', blank=True)


class Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #image = ...

    def __str__(self):
        return f'{self.title}, {self.description} for {self.price}'
    
#comments?