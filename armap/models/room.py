from armap_backend.basemodel import TimeBaseModel
from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator
from .building import Building

class Room(TimeBaseModel):
    name = models.CharField(max_length=100, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6, validators=[MaxValueValidator(90), MinValueValidator(-90)], blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, validators=[MaxValueValidator(180), MinValueValidator(-180)], blank=True, null=True)
    altitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ["-id"]