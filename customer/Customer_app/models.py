from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=15)
    ph_no = models.IntegerField(default=False)
    cust_id = models.IntegerField(default=True, unique=True,primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=10)
    pro_id = models.IntegerField(default=True,unique=True,primary_key=True)

    def __str__(self):
        return self.product_name


class Activity(models.Model):
    state = (
        ('S', 'Sale'),
        ('SR', 'Service'),
    )
    activity = models.CharField(max_length=10, choices=state)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.activity
