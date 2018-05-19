from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media', verbose_name=None, name=None, width_field=None, height_field=None,
                              null=True)


class Schedule(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='schedule')
    week_number = models.IntegerField()
    image = models.ImageField(upload_to='media', verbose_name=None, name=None, width_field=None, height_field=None,
                              null=True)

class Learning(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='learning')
    learning = models.CharField(max_length=100)

class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fee')
    value = models.IntegerField()
