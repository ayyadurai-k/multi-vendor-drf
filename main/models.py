from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name="category_products")
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title
    
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer,related_name="customer_address",on_delete=models.CASCADE)
    address = models.TextField()
    default_address = models.BooleanField(default=False)
    
    def __str__(self):
        return self.address
    
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer,related_name="product_ratings",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="ratings",on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviews = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.rating}-{self.reviews}'