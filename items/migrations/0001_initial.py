# Generated by Django 4.1.1 on 2022-09-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('image', models.ImageField(upload_to='items/')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('genres', models.ManyToManyField(to='items.genres', verbose_name='жанры')),
            ],
        ),
    ]
