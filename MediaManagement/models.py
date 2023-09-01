from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=64)
    image = models.ImageField(upload_to='CategoryImages', blank=True)

class Plan(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='PlanImages', blank=False)
    width = models.CharField(max_length=64)
    height = models.CharField(max_length=64)

class Coordinadas(models.Model):
    lat = models.CharField(max_length=64)
    lng = models.CharField(max_length=64)


class Media(models.Model):
    description = models.CharField(max_length=255)


class MediaContainer(models.Model):
    father_id = models.ForeignKey(Media, on_delete=models.CASCADE)
    son_id = models.ForeignKey(Media, on_delete=models.CASCADE)

class Field(models.Model):
    name = models.CharField(max_length=64, unique=True)

