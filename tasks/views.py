from django.shortcuts import render

def index(request):
    return render(request,"tasks/index.html")

def create(request):
    return render(request,"tasks/create.html")
