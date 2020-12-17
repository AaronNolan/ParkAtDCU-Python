# CA377 parkatdcu Django app

## ParkAtDCU

This ParkAtDCU App is to display real-time information for the carparks in
DCU. This contains:

* Two JSON files used to initiate a DB with objects 
* An API webservice URL to retrieve realtime carpark data


## Extra Functionality

This app also uses Google APIs to retrieve directions from any correctly 
entered address to any of the following carparks:

* Glasnevin
* St. Pats
* All Hallows



## Installation Instructions
### WARNINGS
**WARNING:**  Depending on your local setup 
    **'python'** may be **'python3'**
    
**WARNING:**  Depending on your local setup 
    **'pip'** may be **'pip3'**

### Check these modules are installed:

* Type in terminal: '<b>pip install Pillow</b>'
* Type in terminal: '<b>pip install googlemaps</b>' 


### Instructions:

1. Select Clone -> Copy the <b>Clone with HTTPS</b> URL
2. Go to local terminal and direct to new empty directory where you
wish to store this project
3. In the terminal type: '<b>git clone (paste in url)</b>'
4. When it is cloned go through this path:
<b>2021-ca377-nolana67-parkatdcu -> src -> ca377</b>
5. Type in terminal: '<b>python manage.py migrate</b>'
6. Type in terminal: '<b>python manage.py loaddata ../../data/campus.json</b>' 
7. Type in terminal: '<b>python manage.py loaddata ../../data/carpark.json</b>' 
8. Type in terminal: '<b>python manage.py makemigrations</b>' 
9. Type in terminal: '<b>python manage.py migrate</b>' 
10. Type in terminal: '<b>python manage.py runserver</b>'


## How to run the test cases:

* Go to ca377 directory: <b>2021-ca377-nolana67-parkatdcu -> src -> ca377</b>
* In the terminal type: '<b>python manage.py test</b>'