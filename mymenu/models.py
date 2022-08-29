from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category", blank=True, null=True)
    not_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")
    out_of_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Special(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name

class Exclusive(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    discount = models.IntegerField()
    newprice = models.IntegerField()

    def __str__(self):
        return self.product.name



class Orders(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_qr_cart_total(self):
        orderitems = self.items_set.all()
        total = sum([item.get_qr_total for item in orderitems])
        return total 

    @property
    def get_qr_cart_items(self):
        orderitems = self.items_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_qr_total(self):
        total = self.price * self.quantity
        return total
    
