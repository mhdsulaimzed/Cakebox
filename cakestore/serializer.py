from rest_framework import serializers
from cakestore.models import Cake,Cart,Order,Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Cake
        fields=["id","name","shape","layer","image","weight","price"]

class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields=["id","created_date","user","product","status","quantity"]

class OrderSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    ordered_date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_delivery=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Order
        fields=["id","user","product","ordered_date","address","pincode","status","expected_delivery"]

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"