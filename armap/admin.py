from django.contrib import admin
from armap.models.building import Building
from armap.models.coordinate import Coordinate
from armap.models.route import Route
from armap.models.room import Room
# Register your models here.

admin.site.site_header = "Armap CPanel"
admin.site.site_title = "Armap CPanel"

class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "building", "description"]
    search_fields = ["name"]

class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description"]
    search_fields = ["name"]

class CoordinateAdmin(admin.ModelAdmin):
    list_display = ["lat", "lon"]
    list_filter = ["lat", "lon"]

class RouteAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["name", "category"]

admin.site.register(Room, RoomAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(Route, RouteAdmin)
