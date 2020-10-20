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
    Hostels,
    UploadImage,
    Posts
)

urlpatterns = [
    path('clubs/', Clubs.as_view()),
    path('sports/', Sports.as_view()),
    path('shops/', Shops.as_view()),
    path('socities/', Socities.as_view()),
    path('departments/', Departments.as_view()),
    path('foodcourts/', FoodCourts.as_view()),
    path('placestovisit/', PlacesToVisit.as_view()),
    path('events/', Events.as_view()),
    path('hostels/', Hostels.as_view()),
    path('userposts/', Posts.as_view()),
    path('uploadimage/', UploadImage.as_view())
]
