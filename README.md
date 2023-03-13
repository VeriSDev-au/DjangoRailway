# JangoRailway
This project developed as a template sample on how we can deploy a basic django project into Railway.app platform. It doesn't containt any user interface since the deployment test will be indicated success when the default django page is appear and /admin pages are working (all the static files render properly).


## Prepare Procfile
Procfile as one of the configuration files requested by Railway.App platform. The content of the file depending on the project name when we created Django Project.
Sample file content:

``` py
web: gunicorn DjangoRailway.wsgi --log-file -

```

## Install gunicorn
In the virtual environment, install gunicorn

```cmd
pip install gunicorn
```

## Prepare requirements.txt
Generate this requirements.txt using pip command:

``` cmd
pip list --format=freeze > requirements.txt
```

## Modify settings.py 
In the main project folder (in this project is DjangoRailway folder). We need to add star character to allow to be hosted in any domain or subdomain name within Railway.App.
``` py
ALLOWED_HOSTS = ["*"]
```

## Define STATIC_ROOT
To allow static working within docker in Railway.App we need to install additional library:

``` cmd
pip install whitenoise
```

Within settings.py need to modify static and media file configuration to allow render.

``` py
import os

INSTALLED_APPS = [
    ...
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

## Pulling Static Files
  Run the following command

  ``` cmd
    python manage.py collectstatic
  ```

