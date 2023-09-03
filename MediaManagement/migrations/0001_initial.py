# Generated by Django 4.1 on 2023-09-03 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='CategoryImages')),
            ],
            options={
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Coordinadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=64)),
                ('lng', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'coordinadas',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaManagement.category')),
                ('coordinadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaManagement.coordinadas')),
            ],
            options={
                'verbose_name': 'media',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='PlanImages')),
                ('width', models.CharField(max_length=64)),
                ('height', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'plan',
            },
        ),
        migrations.CreateModel(
            name='MediaContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father_containers', to='MediaManagement.media')),
                ('son', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='son_containers', to='MediaManagement.media')),
            ],
            options={
                'verbose_name': 'media_container',
            },
        ),
        migrations.AddField(
            model_name='media',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaManagement.plan'),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldss', to='MediaManagement.media')),
            ],
            options={
                'verbose_name': 'field',
            },
        ),
    ]
