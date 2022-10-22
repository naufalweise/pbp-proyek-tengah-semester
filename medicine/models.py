from django.db import models

# Create your models here.
class Medicine(models.Model):
	name = models.CharField(max_length=255)
	stock = models.IntegerField()
	pharmacy = models.ForeignKey('pharmacy.Pharmacy', on_delete = models.CASCADE)
