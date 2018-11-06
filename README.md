# Intro
A general purpose Django project for hosting web apps out at Burning Seed

# Set up
Requires a python 3 and I recommend a virtual environment like virtualenvwrapper.

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # follow prompts to create user
python manage.py runserver
```

_Note: currently this uses the default sqlite database, so no db setup is required._
