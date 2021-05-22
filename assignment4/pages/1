from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms
# Create your views here.

def homePageView(request):
	if request.method == "POST":
		artist_form = forms.Artists(request.POST)
		
		if artist_form.is_valid():
			artist_form.save()
			artist_form = forms.Artists()
			
	else:
		artist_form = forms.Artists()

	artist = models.Artists.objects.all()
	context = {
		"body":"2021 Fav Music",
		"artist":artist,
		"form":artist_form
		}
	return render(request, "index.html", context=context);
