# Update System

`sudo apt update`

# Install Python3

`apt install python3`

`sudo apt-get install python3-setuptools`

`sudo apt-get -y install python3-pip`

# Setup Project

`pip3 install -r requirements.txt`

`rm db.sqlite3`

`python3 manage.py migrate`

# Create admin user for login

`python manage.py createsuperuser`

# Start the server

`python3 manage.py runserver`

Access the page at localhost:8000