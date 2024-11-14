from django.shortcuts import render, redirect
from app.models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

def devs(request):
    if request.user.is_authenticated:
        return render(request, 'desenvolvedores.html')
    else:
        return redirect('/admin/login/?next=/')
