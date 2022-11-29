from django.db import models
from django.contrib.auth import get_user_model
from core.models import DeliveryStation, DeliveryManager

from .deliveryproducts import delivery_products

User = get_user_model()


class Place(models.Model):
    displayName = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    address = models.ForeignKey(
        DeliveryStation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pickup_station",
    )

    class Meta:
        verbose_name = "Places"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.displayName or self.address.placeName


class Delivery(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_delivery"
    )
    product = models.CharField(max_length=200, choices=delivery_products)
    pickupPoint = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="fromPoint"
    )
    deliveryPoint = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="toPoint"
    )
    deliverRequestedTime = models.DateTimeField()
    delivered = models.BooleanField(default=False)
    timeOfRequest = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Deliveries"
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return self.user.emailAddress


class ProductDelivery(models.Model):
    manager = models.ForeignKey(
        DeliveryManager, on_delete=models.CASCADE, related_name="delivery_manager"
    )
    delivery = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, related_name="delivery"
    )
    currentLocation = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="delivery_location"
    )
    currentTime = models.DateTimeField()
    delivered = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Deliveries"
        verbose_name_plural = "Product Deliveries"

    def __str__(self):
        return self.manager
