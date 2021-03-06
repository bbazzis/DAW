# Generated by Django 3.1.7 on 2021-04-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_film', models.CharField(max_length=100)),
                ('url_film', models.URLField()),
                ('description', models.CharField(max_length=500)),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=100)),
                ('url_cover', models.URLField()),
                ('num_stars', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('type_user', models.BooleanField()),
            ],
        ),
    ]
