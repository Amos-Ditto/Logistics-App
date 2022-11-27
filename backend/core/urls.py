from django.urls import path
from . import views

urlpatterns = [
    path("register", views.UserView.as_view(), name="user_registration"),
    path("login", views.UserLoginView.as_view(), name="user_login"),
]
