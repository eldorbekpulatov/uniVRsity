from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

def about(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'about.html')

def news(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'news.html')

def sponsors(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'sponsors.html')

def contact(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'contact.html')