# This repo contains my semester project for module CA377

## CA377 parkatdcu Django app

### ParkAtDCU

This ParkAtDCU App is to display real-time information for the carparks in
DCU. This contains:

* Two JSON files used to initiate a DB with objects 
* An API webservice URL to retrieve realtime carpark data


### Extra Functionality

This app also uses Google APIs (API Key needs to be filled to work locally) to retrieve directions from any correctly 
entered address to any of the following carparks:

* Glasnevin
* St. Pats
* All Hallows



### Installation Instructions
#### WARNINGS
**WARNING:**  Depending on your local setup 
    **'python'** may be **'python3'**
    
**WARNING:**  Depending on your local setup 
    **'pip'** may be **'pip3'**

#### Check these modules are installed:

* Type in terminal: '<b>pip install Pillow</b>'
* Type in terminal: '<b>pip install googlemaps</b>' 


#### Instructions:

1. Select Clone -> Copy the <b>Clone with HTTPS</b> URL
2. Go to local terminal and direct to new empty directory where you
wish to store this project
3. In the terminal type: '<b>git clone (paste in url)</b>'
4. When it is cloned go through this path:
<b>ParkAtDCU -> src -> ca377 -> maps</b>
5. In line 9: Replace '<< Enter Google API Key Here >>' with a valid API Key
6. In the terminal type: '<b> cd .. </b>'
7. Type in terminal: '<b>python manage.py migrate</b>'
8. Type in terminal: '<b>python manage.py loaddata ../../data/campus.json</b>' 
9. Type in terminal: '<b>python manage.py loaddata ../../data/carpark.json</b>' 
10. Type in terminal: '<b>python manage.py makemigrations</b>' 
11. Type in terminal: '<b>python manage.py migrate</b>'
12. Go to file: parkatdcu/form.py (<b>cd parkatdcu</b>) and remove all the <b>'# '</b> on the code
 - This was a workaround to an issue stopping the databases from being initialized when the repo was cloned.
13. Type in terminal: '<b>cd ..</b>' (You should now be in directory: <b>ParkAtDCU -> src -> ca377</b>)
13. Type in terminal: '<b>python manage.py runserver</b>'


### How to run the test cases:

* Go to ca377 directory: <b>ParkAtDCU -> src -> ca377</b>
* In the terminal type: '<b>python manage.py test</b>'
