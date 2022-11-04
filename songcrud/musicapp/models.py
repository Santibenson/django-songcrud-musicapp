from django.db import models
import datetime

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    artiste_img_url = models.CharField(max_length=2083, default='', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=500)
    date_released = models.DateTimeField(default=datetime.datetime.now)
    likes = models.IntegerField()
    song_img_url = models.CharField(max_length=2083, default='', blank=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f'Song title: {self.title}'


class Lyric(models.Model):
    content = models.CharField(max_length=5000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
