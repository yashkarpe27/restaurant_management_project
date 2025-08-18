from django.shortcuts import HttpResponse
from django.conf import settings
from django.template import loader

def home(request):
    template = loader.get_template('homepage.html')
    context = {
        'restaurant_name': settings.restaurant_name
    }
    return HttpResponse(template.render(context, request))

def error(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())