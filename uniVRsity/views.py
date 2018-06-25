from django.http import HttpResponse
from django.shortcuts import render
from .models import Member


def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def members(request):
    all_members = Member.objects.all()
    return render(request, 'members.html', {'members': all_members})

def news(request):
    return render(request, 'news.html')

def sponsors(request):
    return render(request, 'sponsors.html')

def contact(request):
    return render(request, 'contact.html')