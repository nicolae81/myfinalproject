from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutUsTemplateView(TemplateView):
    template_name = 'about/about_us.html'
