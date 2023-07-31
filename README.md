# MovieAssignment


INM(International Network of Movies) is a movie review website specially built to provide movie insights,reviews,critics and analytics.One can find movies based on title genre and year.You can also view Movie insights and can add movies to your favourites list so that you won't miss on updates in future.

Technology used:

Django
sqlite
html
css
js
bootstrap


How to setup:

Clone this repository,create a python env with python > 3.9 and install requirements.txt in the repo (command: "pip install -r requirements.txt").


To run the application: 
command on terminal with env activated: "python manage.py runserver" or "python3 manage.py runserver"

To add new movies:
use url "127.0.0.1:8000/admin/"

username: admin
password: admin123

Go to Movies table and add details of new movie,then go back to website and see new movie added under Movies link.

use Login and signup forms for logging in and User creation


open browser and hit "127.0.0.1:8000"



Steps to Deploy the Application:

Get an ec2 instance
clone repo 
configure db and connection using settings.py
set debug = False for production
configure /etc/apt/apache2/sited-enabled/initial.conf ("In ubuntu) with env paths and static and media paths with django configuration
assign elastic ip to your ec2 instance

Hit elastic Ip on browser.The application will be live.
