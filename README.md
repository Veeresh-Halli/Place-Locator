# Introduction

Place Locator is a web application developed using Django and GeoDjango, which allows users to find and manage information about various places. The application utilizes PostgreSQL with PostGIS extension to store geospatial data and Leaflet for interactive map visualization. This documentation provides information on setting up the project, running the server, accessing the admin panel, and testing the API endpoints.

# Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your Ubuntu system:

1. Python 3.9.0     
2. PostGIS extension with the same version as your PostgreSQL(install using `sudo apt-get install postgis postgresql-<version>-postgis-<postgis-version>`).       
3. GeoSpatial Libraries (install using `sudo apt-get install binutils libproj-dev gdal-bin`).

# Project Setup

1. Clone the project repository from GitHub or extract the project files to your desired location.
2. Create a virtual environment (Python 3.9.0) for the project.
3. Activate the virtual environment.
4. Install project dependencies using the requirements.txt file.(`pip install -r requirements.txt`)
5. Open settings.py in the project and configure the database settings under the DATABASES section, providing the required attributes like the database name, username, password, etc.
6. Apply migrations to create the database tables.(`python manage.py makemigrations`, `python manage.py migrate`)
7. Import Karnataka state city coordinates from the places_list.csv file into the PostgreSQL database using the custom management command.(`python manage.py places_to_db`)

# Running the Server

To start the development server, run the following command:

`python manage.py runserver`    

Access the web application by visiting `http://127.0.0.1:8000/` in your browser.

# Admin Panel

The admin panel provides a graphical interface for managing places in the database.       
To access the admin panel, go to `http://127.0.0.1:8000/admin/` in your browser. You'll need to log in with your admin credentials.

# API Endpoints

The project provides several API endpoints to interact with the places data.

# GET Request to Retrieve 50 Places

Endpoint: `http://127.0.0.1:8000/api/places/`     
This endpoint retrieves a paginated list of 50 places by default.

# POST Request to Add a New Place

Endpoint: `http://127.0.0.1:8000/api/places/`      
Request Body:    
```js
{        
    "name": "Pune",       
    "description": "Pune previously known as Poona is a city in Maharashtra state in the Deccan plateau in Western India.",        
    "latitude": "18.53001752",      
    "longitude": "73.85000362"      
}
```                 
Response: `"Pune Place Added Successfully"`

# DELETE Request to Remove a Place

Endpoint: `http://127.0.0.1:8000/api/places/<place_id>/`     
Replace `<place_id>` with the UUID of the place to be deleted.

# GET Request to Search Places by Name or Description

Endpoint: `http://127.0.0.1:8000/api/places/search/?search=<place_name/place_description>`       
Replace `<place_name/place_description>` with the text you want to search for in the place names or descriptions.

The response will contain a list of places that match the search criteria, along with their details.

# Postman Collection

For testing the API endpoints, a Postman collection is provided in the project directory. You can import this collection into Postman to execute and verify the API requests.

That's it 😊! You have successfully set up the Place Locator project using Django, GeoDjango, PostgreSQL, and Leaflet.