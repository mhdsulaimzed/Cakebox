from rest_framework import serializers
from cakestore.models import Cake
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