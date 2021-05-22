from django import forms

from . import models

class Artists(forms.Form):
	artist = forms.CharField(
		label="Artist",
		required=True,
		max_length=240,
	)

	def save(self):
		artist_instance = models.Artists()
		artist_instance.artist = self.cleaned_data["artist"]
		artist_instance.save()
		return artist_instance
