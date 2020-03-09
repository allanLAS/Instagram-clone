from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.urlresolvers import reverse

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        elif not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email)
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    

# Create your models here.
