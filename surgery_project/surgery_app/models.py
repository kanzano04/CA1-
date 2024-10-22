from django.db import models


# Create your models here.


class Surgery(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_opened = models.DateField 


class Patient(models.Model):
    name = models.CharField(max_length=200)
    d_o_b = models.DateField
    surgery = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    no_of_patients = models.IntegerField
    surgery = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:50]
    
