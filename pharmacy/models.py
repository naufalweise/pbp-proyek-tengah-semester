from django.db import models

# Create your models here.
class Pharmacy(models.Model):
	name = models.CharField(max_length=100)


class Medicine(models.Model):
	name = models.CharField(max_length=100)
	stock = models.IntegerField()
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)


	