from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    artiste_img_url = models.CharField(max_length=2083, default='', blank=True)

    def __str__(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=500)
    date_released = models.DateTimeField('date released')
    likes = models.IntegerField()
    song_img_url = models.CharField(max_length=2083, default='', blank=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        if self.title:
            return f'[Song title: {self.title}]  [likes: {self.likes}]'
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length=5000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        if self.song_id:
            return f'{self.song_id}'
        return self.song_id
