from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Client(AbstractUser):
    username = models.CharField(max_length=12, unique=True, null=True)
    # password = models.IntegerField()
    # email = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

Client = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    clients = models.ManyToManyField(Client, related_name='products', blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
