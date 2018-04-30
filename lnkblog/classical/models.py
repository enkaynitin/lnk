from django.db import models
from plans.models import Plan
from materials.models import Wood
from design.models import NeckBodyJoint
import os
# Create your models here.


class Guitar(models.Model):

    plan_name = models.ForeignKey(Plan, on_delete=models.CASCADE)
    voice_sample = models.FileField(upload_to='media', null=True)
    top_plates = models.ForeignKey(Wood, on_delete=models.CASCADE, related_name='guitar_top', null=True)
    back_plates_and_sides = models.ForeignKey(Wood, on_delete=models.CASCADE, related_name='guitar_back', null=True)
    neck_wood = models.ForeignKey(Wood, on_delete=models.CASCADE, related_name='guitar_neck', null=True)
    braces = models.ForeignKey(Wood, on_delete=models.CASCADE, related_name='guitar_braces', null=True)
    neck_joint = models.ForeignKey(NeckBodyJoint,on_delete=models.CASCADE, related_name='neck_to_body_joint', null=True)

    def filename(self):
        return os.path.basename(self.voice_sample.name)

    def __unicode__(self):
        return self.plan_name


class GuitarImage(models.Model):

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=None, name=None, width_field=None, height_field=None, null=True)


class GuitarImage(models.Model):

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media', verbose_name=None, name=None, width_field=None, height_field=None, null=True)