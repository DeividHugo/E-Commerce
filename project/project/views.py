from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def loginView(request):
    return render(request, 'login.html')