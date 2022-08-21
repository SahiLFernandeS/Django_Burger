import re
from django.shortcuts import render, HttpResponse


# Create your views here.
def login_url(request):
    return render(request, 'login.html')


def home_url(request):
    return render(request, "home.html")
