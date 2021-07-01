# Django ToDos App Backend

[![python](https://img.shields.io/badge/Made%20with-Python-1f425f?style=plastic&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-darkgreen?style=plastic&logo=django)](https://docs.djangoproject.com/en/3.2/)
[![djangorestframework](https://img.shields.io/badge/djangorestframework-3.12-blue?style=plastic)](https://www.django-rest-framework.org/)
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=plastic&logo=heroku)](https://django-todos-application.herokuapp.com/api/)

Django To - Dos Application API. Created using `django` and `djangorestframework` and deployed to Heroku.

Endpoint : [https://django-todos-application.herokuapp.com/api/](https://django-todos-application.herokuapp.com/api/)

## Run Server On Local

```bash
python manage.py runserver --setting=TodosBackend.local_settings
```

## Testing

`test.py` for make request testing.

```
usage: test.py [-h] -u URL [-p] [-d DELETE]

Testing script for the backend

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url / endpoint
  -p, --post            Post to Endpoint
  -d DELETE, --delete DELETE
                        Post to Endpoint
```