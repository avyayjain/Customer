from rest_framework import serializers
from .models import Customer, Activity, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'ph_no', 'cust_id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'pro_id']


class ActivitySerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source="customer.name")
    product = serializers.CharField(source="product.product_name")

    class Meta:
        model = Activity
        fields = ['activity', 'customer', 'product']


class ActivitySerializer_post(serializers.ModelSerializer):

    def create(self, validated_data):
        return Activity.objects.create(**validated_data)

    class Meta:
        model = Activity
        fields = ['activity', 'customer', 'product']
