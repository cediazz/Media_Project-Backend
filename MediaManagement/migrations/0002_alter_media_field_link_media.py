# Generated by Django 4.1 on 2023-10-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_field',
            name='link_media',
            field=models.CharField(default='', max_length=255),
        ),
    ]
