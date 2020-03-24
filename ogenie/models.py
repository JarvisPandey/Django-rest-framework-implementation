from django.db import models

# Create your models here.

class query(models.Model):
	quer=models.CharField(max_length=100)


	def __str__(self):
		return self.quer
