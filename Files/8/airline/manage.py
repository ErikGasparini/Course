# python3 manage.py createsuperuser --> Visit the web as an Admin

# Deal With Databases:
# python3 manage.py makemigrations  --> Create a Model with tha tables / changes in "models.py"
# python3 manage.py migrate         --> Apply the migration --> Create the table
# python3 manage.py shell           --> Open a shell to execute python commands

# EXAMPLE
# from flights.models import *
# jfk = Airport(code="JFK", city="New York")
# jfk.save()
# lht = Airport(code="LHR", city="London")
# lht.save()
# f = Flight(origin=jfk, destination=lht, duration=415)
# f.save()

# f.origin.code                     --> Code di Partenza di f
# jfk.departures.all()              --> All the fligths with jfk as departure
# Airport.objects.filter(city="New York")   --> Filter the Airports
# Airport.objects.get(city="New York")      --> Filter if there is 1 Airport

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')
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
