from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import  post
# Create your views here.

class bosh(TemplateView):
    template_name = 'bosh.html'

class kavsar(TemplateView):
    template_name = 'kavsar.html'

class mulk(TemplateView):

    template_name = 'mulk.html'


class rohman(TemplateView):
    template_name = 'rohman.html'

class duo(TemplateView):

    template_name = 'duo.html'

class salovat(TemplateView):

    template_name = 'salovat.html'

class new(ListView):
    model = post

    template_name = 'yangilik.html'

class admin(TemplateView):
    template_name = 'ad.html'


