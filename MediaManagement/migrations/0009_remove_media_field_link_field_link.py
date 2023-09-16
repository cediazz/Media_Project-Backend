# Generated by Django 4.1 on 2023-09-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaManagement', '0008_media_field_link_alter_media_field_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media_field',
            name='link',
        ),
        migrations.AddField(
            model_name='field',
            name='link',
            field=models.CharField(default='', max_length=255),
        ),
    ]