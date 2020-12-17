from django.shortcuts import render
import googlemaps
from datetime import datetime
from .Scripts.time_func import TimeDisFormat
from .models import *
from .form import MapForm

# Google Maps API Key
gmaps = googlemaps.Client(" << Enter Google API Key Here >> ")  # Retrieve API Key and enter here


# DCU Carpark Addresses
carparks = {'1': "DCU multi level parking, Whitehall, Dublin",
            '2': "DCU St Patrick's Campus, Drumcondra Rd Upper, Drumcondra, Dublin 9",
            '3': "DCU Rooms All Hallows, Grace Park Gardens, Drumcondra, Dublin 9"}


# View Functions
# *********************************************************************************************
# View checks if form was filled and if so points to maps_results()
def maps(request):
    status = False
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MapForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            dest = carparks[data['carpark']]
            context = {'form': form}
            context = maps_results(context, data['address'], dest)
            status = True
            context['status'] = status
            return render(request, 'maps/maps.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MapForm()
        context = {'form': form, 'status': status}
        return render(request, 'maps/maps.html', context)


# *********************************************************************************************
# Get directions, format and return to template
def maps_results(context, origin, destination):

    # Handle exceptions from API
    try:
        # Request Directions via Driving from now
        now = datetime.now()
        directions = gmaps.directions(origin,
                                      destination,
                                      mode="driving",
                                      departure_time=now)
        if len(directions) == 0:
            context["err"] = "Error: Address too broad"
            return context
    except googlemaps.exceptions.ApiError:
        context["err"] = "Error: Address Not Found"
        return context
    # Create an array of each step with pre-formatted html syntax, distance and duration
    html_steps = []

    # Get the total duration and distance of the leg (trip) and add to context
    context['duration'] = directions[0]['legs'][0]['duration']['text']
    context['distance'] = directions[0]['legs'][0]['distance']['text']

    # Set values to calculate distance and duration left on each step
    duration = directions[0]['legs'][0]['duration']['value']
    distance = directions[0]['legs'][0]['distance']['value']

    # Predefine path to steps
    steps = directions[0]['legs'][0]['steps']

    # Getting the relevant HTML needed for each step
    i = 1
    for step in steps:
        time, dis = TimeDisFormat(duration, step['duration']['value'], distance,
                                  step['distance']['value']).concatenate()
        duration -= step['duration']['value']
        distance -= step['distance']['value']
        if duration == 0:
            html_steps.append([i, step['html_instructions'], str(dis), "0 min"])
        else:
            html_steps.append([i, step['html_instructions'], str(dis), time])
        i += 1

    context['steps'] = html_steps

    return context
# *********************************************************************************************
