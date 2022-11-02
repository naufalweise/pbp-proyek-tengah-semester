from django.db import models
# Create your models here.
class Market(models.Model):
	promo = models.CharField(max_length=255)