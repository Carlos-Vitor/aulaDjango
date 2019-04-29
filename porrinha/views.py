from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def quemSomos(request):
    return render(request, 'quemSomos.html')
