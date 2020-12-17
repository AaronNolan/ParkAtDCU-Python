from ..models import *
import requests


# Check input is a stored campus and return relevant info
def campus_verify(campus):
    context = {}
    campi = Campus.objects.all()
    found = False
    for camp in campi:  # Go through stored campi
        if campus.lower() == camp.name.lower():  # Define correlating camp object as campus variable
            context["campus"] = camp
            found = True
    if found is False:  # Otherwise return with an err_msg
        context["campus_err_msg"] = "No such campus"
    return context


# Check for corresponding carparks to the campus
def carparks_list(context):
    carparks = Carpark.objects.all()
    no_cps = Campus.objects.filter(campus=None)
    if context["campus"] not in no_cps:
        # Find carparks for this campus
        cp = []
        for carpark in carparks:
            if carpark.campus_id == context["campus"]:
                cp.append(carpark)
        context["carparks"] = cp
    else:
        context["carpark_err_msg"] = "No Carparks Found"
    return context


# Retrieve carpark API data and set up html return info
def carparks_data(context):
    carparks = context["carparks"]
    carpark_data = []
    for carpark in carparks:
        url = "https://jfoster.pythonanywhere.com/carparks/" + str(carpark)
        response = requests.get(url)
        json = response.json()

        if "spaces_available" in json:
            carpark_data.append([carpark, str(json["spaces_available"]) + " spaces"])
        else:
            carpark_data.append([carpark, str("No real time information available")])
    context["cp_data"] = carpark_data
    return context
