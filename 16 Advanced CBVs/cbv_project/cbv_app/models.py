from django.db import models
from django.urls import reverse
# Create your models here.
class Skool(models.Model):
    Name = models.CharField(max_length=128)
    Dean = models.CharField(max_length=128)
    Location = models.CharField(max_length=128)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("cbv:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    Name = models.CharField(max_length=128)
    Age = models.PositiveIntegerField()
    School = models.ForeignKey(Skool, related_name='sisya', on_delete=models.CASCADE)  # name 'sisya' is used in school_detail.html

    def __str__(self):
        return self.Name
