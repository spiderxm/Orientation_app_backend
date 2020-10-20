from django.contrib import admin

from .models import (
    Society,
    Shop,
    Hostel,
    PlaceToVisit,
    PresidentSociety,
    VicePresidentSociety,
    VicePresidentClub,
    PresidentClub,
    Event,
    Sport,
    Club,
    FoodCourt,
    Department,
    UserUpload
)

admin.site.register([
    Society,
    Shop,
    PresidentSociety,
    PlaceToVisit,
    VicePresidentSociety,
    VicePresidentClub,
    Event,
    Sport,
    PresidentClub,
    Club,
    FoodCourt,
    Department,
    Hostel,
    UserUpload
])
