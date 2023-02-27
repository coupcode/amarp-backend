from armap_backend.basemodel import TimeBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models 
from .route import Route


class Coordinate(TimeBaseModel):
    name = models.CharField(max_length=255, unique=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6, validators=[MaxValueValidator(90), MinValueValidator(-90)])
    lon = models.DecimalField(max_digits=9, decimal_places=6, validators=[MaxValueValidator(180), MinValueValidator(-180)])

    def __str__(self):
        return f"{self.name} ({self.lat}, {self.long})"