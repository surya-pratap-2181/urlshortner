from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.CharField(_('Mobile Number'), unique=True, max_length=12, null=True)
    invited_by = models.CharField(max_length=12, blank=False, default='shortly')
    invite_query = models.CharField(max_length=12, blank=False, default='shortly')
    coin = models.IntegerField(default=0)