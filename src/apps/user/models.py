from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
