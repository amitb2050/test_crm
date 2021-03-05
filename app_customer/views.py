# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer


# Create your views here.  
def create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'app_customer\create.html', {'form': form})
    else:
        form = CustomerForm()
    return render(request, 'app_customer\create.html', {'form': form})


def index(request):
    customers = Customer.objects.all()
    return render(request, "app_customer\index.html", {'customers': customers})
