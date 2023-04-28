from django.contrib import admin
from cakestore.models import Cake,Cart,Order,Review

# Register your models here.
admin.site.register(Cake)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Review)
