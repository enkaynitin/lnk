from django.db import models

# Create your models here.


class NeckBodyJoint(models.Model):

    name = models.CharField(max_length=50, null=True)
    history = models.CharField(max_length=1000, null=True)
    features = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name

# class Bridge(models.Model):

