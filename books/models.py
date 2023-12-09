from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    favorites = models.ManyToManyField('Book', related_name='favorites', blank=True)
    cart = models.ManyToManyField('Book', related_name='cart', blank=True)
    #image = models.ImageField(upload_to='images/profile', blank=True)
    #description = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profile', blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
    
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