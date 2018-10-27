from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
	template_name = 'inicio.html'

def LogOut(request):
	logout(request)
	return redirect('/')	