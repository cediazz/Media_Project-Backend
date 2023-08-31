from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from Security.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Permission)
#admin.site.register()
