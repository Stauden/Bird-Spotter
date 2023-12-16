# Bird Spotter

#Description

Bird Spotter is a Django-based project that creates a vibrant community for bird enthusiasts. It's designed for sharing and documenting bird sightings and information. Whether you're an avid birder or just enjoy occasional glimpses of avian beauty, Bird Spotter offers a platform to record and share your experiences.

#Features
* User Profiles: Create your own birding profile and connect with fellow bird lovers.
* Bird Logging: Easily log your bird sightings, complete with species, time, and location data.
* Photo Uploads: Share your bird photographs with the community.

#Usage
1. Registration: Sign up for an account to start contributing.
2. Document a Sighting: Log your bird sightings and upload pictures.
3. Explore: Browse the homepage to see recent sightings and photos from other users.

#Get Started 
1.Prerequisites
  * Python Version: 3.11.5
  * Django Version: 4.2.7
2. Installation
  * Clone the Repository
  * Django setup Guide: https://docs.djangoproject.com/en/4.2/topics/install/
  * Install Pillow with pip: https://pillow.readthedocs.io/en/latest/installation.html 
    * python3 -m pip install --upgrade pip
    * python3 -m pip install --upgrade Pillow
  * Command to run Django's development server: python manage.py runserver

#Goals
The Bird Spotter project is currently in an exploratory phase. We're still experimenting with different features and directions. This means that the project might evolve as we learn more and receive feedback from the community. However, Please note that Bird Spotter is a project initiated as a personal exploration and may not have plans to bring it to full completion. It serves as a platform for learning and experimentation.

#Current Status
  * Alpha Stage
  * Project is not feature complete 

#Known Bugs
* When deleting all posts it deletes status (there's no model / task to save too)
* Empty bullets: caused by empty status / data variable and more html work on home view would solve. 

#Contributers 
- Jordan S - https://github.com/Stauden
