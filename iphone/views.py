from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def iphone(request):
    return HttpResponse('This page for Iphone !!')
