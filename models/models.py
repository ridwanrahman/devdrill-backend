from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    This model is added so that I can add more fields/attributes here
    if need be later on.
    I used UserAdmin to show it nicely in the admin panel. But new fields won't show up
    check stackoverflow.
    """
    pass

