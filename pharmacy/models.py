from django.db import models
from django.conf import settings

# Create your models here.
class Pharmacy(models.Model):
	name = models.CharField(max_length=255)
	address = models.TextField()

	def __str__(self) -> str:
		return self.name