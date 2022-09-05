from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Powdered Mushroom', 'Powdered Mushroom'),
        ('Canned Mushroom', 'Canned Mushroom'),
        ('Mushroom Mchuzi', 'Mushroom Mchuzi'),
        ('Fresh Mushroom', 'Fresh Mushroom'),
        ('Mushroom Juice', 'Mushroom Juice'),

    )
    name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    # class Meta:
    #     ordering = ('date_created')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("Pending", 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ("Delivered", 'Delivered'),
    )
    customers = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.status
