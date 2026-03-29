from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_registration(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=200)
    type=models.CharField(max_length=20,choices=[('admin','admin'),('user','user')],default='user')

class product(models.Model):
    CATEGORY_CHOICES=[('men','Men'),('women','Women'),('kids','Kids')]
    pdt_name=models.CharField(max_length=200)
    image=models.FileField(upload_to='pic')
    description=models.TextField()
    price=models.CharField(max_length=10)
    category=models.CharField(max_length=10,choices=CATEGORY_CHOICES)

class Cart(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     phone=models.CharField(max_length=15)
#     adress=models.TextField()
    