from django.shortcuts import HttpResponse
from django.conf import settings
from django.template import loader

def home(request):
    template = loader.get_template('homepage.html')
    context = {
        'restaurant_name': settings.restaurant_name
    }
    return HttpResponse(template.render(context, request))