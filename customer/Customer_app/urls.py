from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"customer", views.CustomerDetails, basename="CustomerDetails")
router.register(r"product", views.ProductDetails, basename="ProductDetails")
router.register(r"activity", views.ActivityDetails, basename="ActivityDetails")

urlpatterns = []
urlpatterns += router.urls
