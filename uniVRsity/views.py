from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')