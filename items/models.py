from django.db import models


# Create your models here.


class Genres(models.Model):
    name = models.CharField(max_length=250, verbose_name='Жанр')


    class Meta:
        verbose_name='Жанры'
    def __str__(self):
        return self.name


class Items(models.Model):
    title = models.CharField('Название', max_length=250)
    image = models.ImageField(upload_to="items/")
    genres = models.ManyToManyField(Genres, verbose_name='жанры')
    price = models.IntegerField()
    description = models.TextField()