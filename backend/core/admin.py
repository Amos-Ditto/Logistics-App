from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, DeliveryManager, DeliveryStation
from .forms import UserChangeForm, UserCreationForm

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["emailAddress", "fullName", "is_admin"]
    list_filter = ("is_admin",)

    fieldsets = (
        ("Authentication", {"fields": ("emailAddress",)}),
        ("Personal Info", {"fields": ("fullName",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("emailAddress", "fullName", "password1", "password2"),
            },
        ),
    )

    search_fields = (
        "emailAddress",
        "fullName",
    )
    ordering = ("emailAddress",)
    filter_horizontal = ()


@admin.register(DeliveryStation)
class DeliveryStationAdmin(admin.ModelAdmin):
    list_display = ["id", "placeName", "region", "town", "active"]


@admin.register(DeliveryManager)
class DeliveryManagerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "station", "active"]
