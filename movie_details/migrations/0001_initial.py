# Generated by Django 4.1.4 on 2022-12-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Year', models.CharField(blank=True, max_length=25)),
                ('Rated', models.CharField(blank=True, max_length=10)),
                ('Genre', models.CharField(blank=True, max_length=255)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Actors', models.CharField(blank=True, max_length=255)),
                ('Plot', models.CharField(blank=True, max_length=900)),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
    ]
