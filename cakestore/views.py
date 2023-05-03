from django.shortcuts import render
from django.contrib.auth.models import User
from cakestore.serializer import UserSerializer,CakeSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework .mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from cakestore.models import Cake,Cart,Order
from rest_framework import serializers
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class UserCreateView(CreateModelMixin,GenericViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()



class CakeView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]



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
   
   
    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        serializer=CartSerializer(data=request.data)
        p=self.get_object()
        user=request.user
        if serializer.is_valid():
            serializer.save(user=user,product=p)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    @action(methods=["post"],detail=True)
    def place_order(self,request,*args,**kwargs):
        serializer=OrderSerializer(data=request.data)
        p=self.get_object()
        user=request.user
        if serializer.is_valid():
            serializer.save(user=user,product=p)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
  
  
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        sz=ReviewSerializer(data=request.data)
        p=self.get_object()
        user=request.user
        if sz.is_valid():
            sz.save(user=user,product=p)
            return Response(data=sz.data)
        else:
            return Response(data=sz.errors)
        
        
class CartListView(GenericViewSet,ListModelMixin):
    serializer_class=CartSerializer
    queryset=Cart.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        qs=Cart.objects.filter(user=request.user)
        sz=CartSerializer(qs,many=True)
        return Response(data=sz.data)



class OrderListView(GenericViewSet,ListModelMixin):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        qs=Order.objects.filter(user=request.user)
        sz=OrderSerializer(qs,many=True)
        return Response(data=sz.data)


