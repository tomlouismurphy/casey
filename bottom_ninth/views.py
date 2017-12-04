from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Batter, Pitcher

class IndexView(generic.ListView):
	template_name = 'bottom_ninth/index.html'
	def get_queryset(self):
		return Batter.objects.order_by('id')

class DetailView(generic.DetailView):
	model = Batter
	template_name = 'bottom_ninth/detail.html'

