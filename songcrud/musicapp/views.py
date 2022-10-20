from django.shortcuts import render
from django.http import HttpResponse

def music(request):
    return HttpResponse("<h1>Hello, Zuri</h1>")