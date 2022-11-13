from django.contrib import admin

from .models import Customer, Product, Activity


# Register your models here.
@admin.register(Customer)
class Customer_Admin(admin.ModelAdmin):
    list_display = ['name', 'ph_no', 'cust_id']


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ['product_name', 'pro_id']


@admin.register(Activity)
class Activity_Admin(admin.ModelAdmin):
    list_display = ['activity', 'customer', 'product']
