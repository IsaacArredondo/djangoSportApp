from django.shortcuts import render
from .forms import DataForm

# Create your views here.

def index(request):
    form = DataForm()
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/index.html', context)

def predictions(request):
    return render(request, 'dashboard/predictions.html')