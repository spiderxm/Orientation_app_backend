from django.conf.urls import url
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

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Gaze NITH Api",
        default_version='v1',
        description="Api To get details for NITH And various social activities",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mrigank.anand52@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
