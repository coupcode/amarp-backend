from armap_backend.basemodel import TimeBaseModel
from django.db import models 

class Route(TimeBaseModel):
    MAIN_ROUTE = "Main route"
    ROUGH_ROUTE = "Rough route"
    STAIR_CASE_ROUTE = "Stair case route"

    ROUTE_CATEGORY_LIST = [
        (MAIN_ROUTE, MAIN_ROUTE),
        (ROUGH_ROUTE, ROUGH_ROUTE)
    ]
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=100, default=MAIN_ROUTE, choices=ROUTE_CATEGORY_LIST)

    def __str__(self):
        return f"{self.name} ({self.category})"