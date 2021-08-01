# Django ToDos App Backend

[![python](https://img.shields.io/badge/Made%20with-Python-1f425f?style=plastic&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-darkgreen?style=plastic&logo=django)](https://docs.djangoproject.com/en/3.2/)
[![djangorestframework](https://img.shields.io/badge/djangorestframework-3.12-blue?style=plastic)](https://www.django-rest-framework.org/)
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=plastic&logo=heroku)](https://django-todos-application.herokuapp.com/api/)

Django To - Dos Application API. Created using `django` and `djangorestframework` 
and deployed to Heroku.

Endpoint : [https://django-todos-application.herokuapp.com/api/](https://django-todos-application.herokuapp.com/api/)

## Run Server On Local

Install requirements

```bash
pip install -r local-requirements.txt
```

Update the `DEV_USERNAMES` in the `settings.py` with username on the local computer

```python
DEV_USERNAMES = [
    'hyuto',
    'Wahyu Setianto',

    'NEW-USERNAME'
]

...
```

then do migration and run the server 

```bash
python manage.py migrate
python manage.py createsuperuser # for creating super user
python manage.py runserver
```

## Testing

`test/test-api.py` for make request testing.

```
usage: test-api.py [-h] -u URL [-l] [-r] [-g] [-p] [-t PUT] [-d DELETE]

Testing script for the backend

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url / endpoint
  -l, --login           Login
  -r, --register        Register
  -g, --get             GET
  -p, --post            Post to Endpoint
  -t PUT, --put PUT     Put to Endpoint
  -d DELETE, --delete DELETE
                        Post to Endpoint
```

## To Do

1. Make authentication using `JWT`