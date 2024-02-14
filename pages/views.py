from django.shortcuts import render
from django.http import HttpResponse
 def homePageView(request): # new •     
    return HttpResponse('Hello World!') # new