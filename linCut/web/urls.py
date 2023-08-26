from django.urls import  path
from .views import index, getLink

urlpatterns = [
    path('',index, name='home'),
    path('<str:link>',getLink,name='getLink')
]
