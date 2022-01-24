from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from . manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField('First name', blank=True, null=True, max_length=250)
    last_name = models.CharField('Last name', blank=True, null=True, max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Указано, что все объекты для класса поступают из CustomUserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.email