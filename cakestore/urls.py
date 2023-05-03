from django.urls import path
from cakestore import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("user/register",views.UserCreateView,basename="usercreate")
router.register("cake",views.CakeView,basename="cake")
router.register("mycart",views.CartListView,basename="cartlist")
router.register("myorder",views.OrderListView,basename="orderlist")
                


urlpatterns = [
    path("token/",ObtainAuthToken.as_view()),
    


]+router.urls


#{
  #eae78aebbb6453697f9e664b161c9cac7a60f263
