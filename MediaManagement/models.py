from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=64)
    image = models.ImageField(upload_to='CategoryImages', blank=True)
    class Meta:
        verbose_name = 'category'

class Plan(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='PlanImages', blank=False)
    width = models.CharField(max_length=64)
    height = models.CharField(max_length=64)
    class Meta:
        verbose_name = 'plan'

class Coordinadas(models.Model):
    lat = models.CharField(max_length=64)
    lng = models.CharField(max_length=64)
    class Meta:
        verbose_name = 'coordinadas'


class Media(models.Model):
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    coordinadas = models.ForeignKey(Coordinadas, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'media'


class MediaContainer(models.Model):
    father = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='father_containers')
    son = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='son_containers')
    class Meta:
        verbose_name = 'media_container'

class Field(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=128,default='')
    media = models.ForeignKey(Media, related_name='fieldss', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'field'




