from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Tailor(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    time_from_week = models.PositiveSmallIntegerField(verbose_name="godzina otwarcia w tygodniu")
    time_to_week = models.PositiveSmallIntegerField(verbose_name="godzina zamknięcia w tygodniu")
    time_from_weekend = models.PositiveSmallIntegerField(verbose_name="godzina otwarcia w weekend")
    time_to_weekend = models.PositiveSmallIntegerField(verbose_name="godzina zamknięcia weekend")



class Grades(models.Model):
    grade = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    tailor = models.ForeignKey(Tailor,  on_delete=models.CASCADE)





