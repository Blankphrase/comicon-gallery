world of comicon
===================
## Description
[World of comicon](https://github.com/jakhax/comicon-gallery.git) is a personal gallery application that you display your superhero and villain photos for others to see.

------------------------------------------------------------------------

## User Requirements

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image model and copy link button.
+ [x] Filter images based on category and location.
+ [x] search functionality based on image description.

## TODO
+ [ ] Work on the front-end of the app (Add more css styling to the app other than the basic bootstrap)
+ [ ] Add commenting on images feature
+ [ ] Add tagging feature
+ [ ] Rank images during search


## Models
### Image Model
* Fields: Image, Image Name, Image Description, Image Location Foreign Key and Image category Foreign Key.

* `save_image()` - Save an image to the database.
* `delete_image()` - Delete image from the database.
* `update_image()` - Update image in the database.
* `get_image_by_id(id)` - Allows us to get an image using its ID.
* `search_image(category)` - Allows us to search for an image using its category.
* `filter_by_location(location)` - Allows us to filter images by the location.

### Location and Category models
* Location and category that link to the Image model.
* `save`, `update` and `delete` methods in both models

## Admin Dashboard
Use django admin to post photos to the database and manage the photos

## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/jakhax/pitches.git && cd pitches
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Running the server 
```bash
python manage.py runserver
```

### Deploying to heroku
Refer to this guide: [deploying to heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)
Set the configuration to production mode


## Live Demo

The web app can be accessed from the following link: 
[World of Comicon](https://worldofcomicon.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 2.0.2](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)


## Contributing

- Git clone [https://github.com/jakhax/comicon-gallery.git](https://github.com/jakhax/comicon-gallery.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Jack ogina](https://github.com/jakhax)