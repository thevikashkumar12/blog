from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def LCD(request):
    return render(request, "LCD.html")


def fridge(request):
    return render(request, "fridge.html")


def washing(request):
    return render(request, "washing.html")


def mobile(request):
    return render(request, "mobile.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        query = request.POST.get("query")
        contact = Contact(name=name, email=email, phone=phone, query=query, date=datetime.today())
        contact.save()
        messages.success(request, "Your query has been submitted")
        
    return render(request, "contact.html")