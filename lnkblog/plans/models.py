from django.db import models

# Create your models here.


class Plan(models.Model):

    name = models.CharField(max_length=30)
    luthier_name = models.CharField(max_length=30, null=True)
    year = models.IntegerField()
    location = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
