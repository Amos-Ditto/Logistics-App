from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, emailAddress, password=None):
        if not emailAddress:
            raise ValueError("You must enter Email Address")

        user = self.model(emailAddress=emailAddress)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emailAddress, password=None):
        user = self.create_user(emailAddress, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    emailAddress = models.EmailField(unique=True, primary_key=True)
    fullName = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "emailAddress"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self) -> str:
        return self.emailAddress

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
