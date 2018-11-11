from rest_framework import serializers
from .models import Product, Category, Client
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    # clients = ClientSerializer(many=True)
    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True)
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, required=False)
    class Meta:
        model = Client
        fields = ('username', 'password', 'email', 'products')

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = '__all__'
