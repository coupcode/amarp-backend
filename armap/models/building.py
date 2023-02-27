from django.db import models
from armap_backend.basemodel import TimeBaseModel
# Create your models here.

class Building(TimeBaseModel):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(blank=True)
    
    front_view_lat = models.CharField(max_length=255, null=True, blank=True)
    front_view_long = models.CharField(max_length=255, null=True, blank=True)
    
    left_view_lat = models.CharField(max_length=255, null=True, blank=True)
    left_view_long = models.CharField(max_length=255, null=True, blank=True)
    
    right_view_lat = models.CharField(max_length=255, null=True, blank=True)
    right_view_long = models.CharField(max_length=255, null=True, blank=True)
    
    back_view_lat = models.CharField(max_length=255, null=True, blank=True)
    back_view_long = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ["-id"]
        
