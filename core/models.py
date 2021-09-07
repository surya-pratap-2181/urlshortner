from django.db import models
from accounts.models import CustomUser
# Create your models here.


class ShortURL(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
