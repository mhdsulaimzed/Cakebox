from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Cake(models.Model):
    name=models.CharField(max_length=200)
    option=(
        ("round","round"),
        ("square","square"),
        ("rectangle","rectangle")
    )
    shape=models.CharField(max_length=200,choices=option,null=True,)
    layer = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
     )
    image=models.ImageField(upload_to="images",null=True,blank=True)
    weight=models.FloatField(default=1)
    price=models.PositiveIntegerField()

    @property
    def cake_reviews(self):
        return Review.objects.filter(product=self)
        

    def __str__(self):
        return self.name

class Cart(models.Model):
    product=models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    statusoptions=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=statusoptions,default="in-cart")
    quantity=models.PositiveIntegerField(default=1)


class Order(models.Model):
    product=models.ForeignKey(Cake,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    ordered_date=models.DateField(auto_now_add=True)
    pincode=models.PositiveIntegerField()
    statusoptions2=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    
    status=models.CharField(max_length=30,choices=statusoptions2,default="order-placed")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    curdate=datetime.date.today()
    eta=curdate+datetime.timedelta(days=5)
    expected_delivery=models.DateField(default=eta)


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Cake,on_delete=models.CASCADE,related_name="cakereview")
    comment=models.CharField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment


#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