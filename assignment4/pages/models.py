from django.db import models

# Create your models here.

class Artists(models.Model):
	artist = models.CharField(max_length=240)

	def __str__(self):
		return self.artist
