from django.contrib import admin
from .models import Place, Delivery, ProductDelivery


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["id", "displayName", "longitude", "latitude"]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "product",
        "pickupPoint",
        "deliveryPoint",
        "deliverRequestedTime",
        "delivered",
        "timeOfRequest",
    ]


@admin.register(ProductDelivery)
class ProductDeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "manager",
        "delivery",
        "currentLocation",
        "currentTime",
        "delivered",
    ]
