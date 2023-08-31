from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager


"""class CustomUser(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password = models.C
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')"""

class MyUserManager(BaseUserManager):
    def _create_user(self,username,password,is_active,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            is_active = is_active,
            is_staff =  is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_user(self,username,password = None,**extra_fields):
        return self._create_user(username,password,True,False,False,**extra_fields)

    def create_superuser(self,username,password = None,**extra_fields):
        return self._create_user(username, password,True, True, True, **extra_fields)




class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
   # groups = models.ManyToManyField(Group, related_name='customuser_set')
    #user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username




