from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Client#, User #123

# admin.site.register(User)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
