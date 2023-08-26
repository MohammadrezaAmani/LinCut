from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Link


# Create your views here.
def index(request,*args, **kwargs):
    return JsonResponse({
        'message':'hello world!'
    })
    
def getLink(request, link:str, *args, **kwargs):
     li = Link.objects.filter(shortedLink=link)
     return JsonResponse({'list':li[0].link})