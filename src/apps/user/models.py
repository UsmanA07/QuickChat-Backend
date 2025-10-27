from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    def __str__(self):
        return self.username
