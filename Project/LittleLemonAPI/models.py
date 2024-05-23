from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('manager', 'manager'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.user.username
    
    


    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.profile.save()

class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
        
    def __str__(self) -> str:
         return f"{self.first_name} {self.last_name}"



class Category(models.Model):
    name = models.CharField(max_length=255)
    
   
    
    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.CharField(max_length=250) 
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return f"Order by {self.user.username} for {self.product.name}"
    
    
  
    
    

    

    
    
    
    


