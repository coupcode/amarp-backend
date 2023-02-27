from armap_backend.basemodel import TimeBaseModel
from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator
from armap.models.route import Route

class RouteMapping(TimeBaseModel):
    name = models.CharField(max_length=100, unique=True)
    routes = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return self.name 
    