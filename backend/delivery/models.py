from django.db import models


class Place(models.Model):
    displayName = models.CharField(max_length=255)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Places"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.displayName
