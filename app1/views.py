from django.shortcuts import render
from app1.models import *
from django.views.generic import ListView
# Create your views here.
class schoollist(ListView):
    model=School
    context_object_name='schools'
    #template_name='app1/school_list.html'
    #queryset=School.objects.filter(name='Jspiders')
    ordering=['name']