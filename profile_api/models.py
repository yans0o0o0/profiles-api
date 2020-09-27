from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manager for Users Profile """

    def create_user(self, email, name, lastname, password):

        # normalize the email address passed to the create user function
        email = self.normalize_email(email)

        user = self.model(email=email,name=name,lastname=lastname)

        # before set the password we need to make sure wont be saved as plain
        # text, so we can use django 'set_password' to make the password a hash
        user.set_password(password)

        # we could use only user.save() but using=self.__db is to specify
        # the db in which the user will be saved in case we are using multiple
        # dbs, self.__db is the standard db.
        #user.save(using=self.__db)
        user.save()

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True

        # we could use only user.save() but using=self.__db is to specify
        # the db in which the user will be saved in case we are using multiple
        # dbs, self.__db is the standard db.
        #user.save(using=self.__db)
        user.save()

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Model for users in the System """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name'] # email is required as is Username CharField

    def get_full_name(self):
        """ Retrieve the full name of the user """
        return str(self.name)+" "+str(self.lastname)

    def get_short_name(self):
        """ Retrieve the name of the user """
        return self.name

    def __str__(self):
        """ The string representation of our model """
        return self.email
