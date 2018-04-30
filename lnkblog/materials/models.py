from django.db import models

# Create your models here.


class Wood(models.Model):
    name = models.CharField(max_length=50, null=True)
    strength = models.FloatField(null=True)
    specific_gravity = models.FloatField(null=True)

    def __unicode__(self):
        return self.name


class NutAndSaddle(models.Model):
    material = models.CharField(max_length=20)
    density = models.FloatField(null=True)

    def __unicode__(self):
        return self.material


class TuningMachine(models.Model):
    type = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    def __unicode__(self):
        return self.type
