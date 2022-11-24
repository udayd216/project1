from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app_uday(request):
    return HttpResponse('<h1><marquee><i><mark>i am uday</mark></i></marquee></h1>')