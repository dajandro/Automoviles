from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Marca(models.Model):
	"""docstring for Carros"""
	name = models.CharField(max_length = 50)
	country = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class Automovil(models.Model):
	"""docstring for Automovil"""
	marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
	tipo = 	models.CharField(max_length = 50)
	year = models.IntegerField(default = 1950)
	

	def __str__(self):
		return self.marca, self.tipo, self.year
