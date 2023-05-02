from django.urls import path
from cakestore import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("user/register",views.UserCreateView,basename="usercreate")
router.register("cake",views.CakeView,basename="cake")
                


urlpatterns = [
    


]+router.urls