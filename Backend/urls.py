from django.urls import path, include
from .views import (
    Clubs,
    Sports,
    Shops,
    Socities,
    Departments,
    FoodCourts,
    PlacesToVisit,
    Events,
    Hostels

)

urlpatterns = [
    path('clubs/', Clubs.as_view()),
    path('sports/', Sports),
    path('shops/', Shops),
    path('socities/', Socities),
    path('departments/', Departments),
    path('foodcourts/', FoodCourts),
    path('placestovisit/', PlacesToVisit),
    path('events/', Events),
    path('hostels/', Hostels)
]
