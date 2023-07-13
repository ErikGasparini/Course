# django-admin startproject ProjectName     :Create writting in the terminal
# python3 manage.py runserver               :Lunch server
# python3 manage.py startapp AppName        :Create an App insede the project

# File to modify - Main
# settings.py   --> Add in INSTALLED_APPS
# urls.py       --> Include to urlpatterns

# File to modify - Apps
# views.py      --> Create functions and HttpResponse() or render()
# urls.py       --> Add to urlpatterns

# Table: django_session --> Avoid Errors typing:
# python3 manage.py migrate --> Create default Tables


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lecture4.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
