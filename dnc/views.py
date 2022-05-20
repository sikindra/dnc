from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def faq(request):
    return render(request, "faq.html")


def service(request):
    return render(request,"service.html")    


def contact(request):
    return render(request,"contact.html")


def pricing(request):
    return render(request, "pricing.html")


def blog(request):
    return render(request,"blog.html")