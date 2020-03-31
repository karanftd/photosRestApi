# PhotosRestApi

Write a Django app called photos, and provide API to accomplish following features.


## Main features:
- [x] Post a photo.
- [x] Save photos as draft.
- [x] Edit photo captions.
- [x] Delete photos.
- [x] List photos (all, my photos, my drafts)
- [x] ASC/DESC Sort photos on publishing date
- [x] Filter photos by user.
- [x] Limit the uploaded photo size to a certain maximum dimensions and bytes.
- [x] JWT authentication.
- [x] Host it somewhere like Heroku or PythonAnywhere.com, both offer free hosting for python apps.
- [x] Maintain a good git history.

### Requirement
```
Pyhton 3.7+
```
### Install dependencies
```
pip install -r requirements.txt
```

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/token/` | Request jwt token


#### Photo Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/photo/` | List users's photos
POST | `/photo/` | Uploda photo to user account
GET | `/photo?user=all` | all the user's photos
GET | `/photo?user={username}` | Retrieve photos of {username}
PATCH | `/photo/{id}` | Edit a photo details
DELETE | `//photo/{id}` | Delete a photo

## Installation Guide
If you wish to run your own build, you two options
 1. Use Docker.
    
    `$ git clone https://github.com/karanftd/photosRestApi.git`
    
    `$ cd photosRestApi`    
    `$ docker build -t hmlet .`
    `$ docker run -e AWS_ACCESS_KEY_ID={aws_key} AWS_SECRET_ACCESS_KEY={aws_secret} hmlet`
 
 2. Without docker
 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/karanftd/photosRestApi.git
    $ cd photosRestApi
Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

### Launching the app
    $ python manage.py runserver

-----------------

## TOOLS

##### Backend Development:
Django RESTful

##### Deployment
Docker | Heroku | Circle CI | AWS S3 | Cloudflare(DNS)

##### Database Development:
Postgres | SQLite

-----------------

## DEMO
- Admin Login, Upload Photos.
> https://www.loom.com/share/e68abf6ba7cd4eb28f8729662029dd28
- List photos, filter by Published/Draft, create User, list all photos, list all users photos, list selected User photos.
> https://www.loom.com/share/55709c620a7643aa8b80cb9a099650ff
- Delete photo, update status, update caption, show uploaded photos.
> https://www.loom.com/share/bffa92e057c948c681eed80f3ee26006
- Sort photos by ASC/DESC and overview of solution(diving into codebase).
> https://www.loom.com/share/69f448638b8e43cd91c5a9a6eed74fc3
- Infrastructure overview, hosting overview and Circle-CI setup.
> https://www.loom.com/share/400b47c154a3425c87677231bc5ec4bf


<br/>
Thank you,
<br/>
Karan Bhalodiya
