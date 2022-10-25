from django.shortcuts import render
from django.http import HttpResponse

def music(request):
    return render(request, 'index.html')