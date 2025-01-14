"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings"
)

from configurations.wsgi import get_wsgi_application  # noqa isort:skip

application = get_wsgi_application()
