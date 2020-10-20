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
    path('sports/', Sports.as_view()),
    path('shops/', Shops),
    path('socities/', Socities.as_view()),
    path('departments/', Departments),
    path('foodcourts/', FoodCourts),
    path('placestovisit/', PlacesToVisit),
    path('events/', Events),
    path('hostels/', Hostels)
]
