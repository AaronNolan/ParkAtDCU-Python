from django.shortcuts import render, redirect
import requests
from .models import *
from .form import *
from .Scripts.campus_verify import *


# Create your views here.
def index(request):
    form = CarparkForm()
    context = {'form': form}
    return render(request, 'parkatdcu/index.html', context)


def carparks(request):
    campus = request.GET["campus"]
    context = campus_verify(campus)  # Verify input for campus data correlates to a stored value
    if "campus" in context:  # If it does
        context = carparks_list(context)  # Retrieve a list of the that campus's carpark objects
        if "carparks" in context:  # If it returns with carparks
            context = carparks_data(context)  # Get the restapi data
    return render(request, "parkatdcu/carparks.html", context)
