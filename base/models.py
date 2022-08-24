from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self) :
        return self.name


class Product(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    photo=models.ImageField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self) :
        return self.description


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.address


class Cart(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True, db_column='username')
    cat=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    prod=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    amount= models.DecimalField(max_digits=100,decimal_places=2 ,default=1)
    total_price= models.DecimalField(max_digits=100,decimal_places=2, default=0)
       # image?
    def __str__(self) :
        return self.cat


class Order(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    cat=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    prod=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    amount=models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True, related_name='order_amount', db_column='amount')
    total_price= models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True,related_name='order_total_price',db_column='total_price')
    createdTime=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.cat
    

# class Discount(models.Model):
#     pass

