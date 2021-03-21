import dramatiq

from .models import Link


@dramatiq.actor
def do_something():
    ...
