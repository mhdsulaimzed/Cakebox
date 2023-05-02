from django.shortcuts import render
from django.contrib.auth.models import User
from cakestore.serializer import UserSerializer,CakeSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework .mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from cakestore.models import Cake
from rest_framework import serializers


# Create your views here.
class UserCreateView(CreateModelMixin,GenericViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


class CakeView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()


    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method not allowed")
    
    def get_queryset(self):
        qs=Cake.objects.all()

        if "layer" in self.request.query_params:
            lyr=self.request.query_params.get("layer")
            qs=qs.filter(layer=lyr)

        if "shape" in self.request.query_params:
            shp=self.request.query_params.get("shape")
            qs=qs.filter(shape=shp)
        return qs
