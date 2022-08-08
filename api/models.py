from django.db import models

# Create your models here.
class Mahsulotlar(models.Model):
	mahsulot_nomi = models.CharField(max_length=200)
	mahsulot_tarkibi = models.TextField()
	mahsulot_rasmi = models.ImageField(upload_to='images/')
	mahsulot_narxi = models.CharField(max_length=10)

	def __str__(self):
		return self.mahsulot_nomi