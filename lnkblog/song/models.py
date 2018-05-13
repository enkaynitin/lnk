from django.db import models

# Create your models here.


class Scale(models.Model):
    key = models.CharField(max_length=2)
    pattern = models.CharField(max_length=50)

    def __unicode__(self):
        return "{} {}".format(self.key, self.pattern)


class Song(models.Model):

    record = models.FileField(upload_to='media', null=True)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    lyrics = models.TextField()
    lyrics_syllables = models.TextField()

    def __unicode__(self):
        return self.scale


class MusicNotations(models.Model):

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    staff_notation = models.TextField()

    def __unicode__(self):
        return "{} {}".format(self.song, self.staff_notation)









