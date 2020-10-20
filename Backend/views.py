from rest_framework.views import APIView
from .models import Club
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Society, Sport, Shop, Hostel, Department, PlaceToVisit, Event, FoodCourt
from .serializers import (SocietySerializer,
                          SportSerializer,
                          ShopSerializer,
                          DepartmentSerializer,
                          HostelSerializer,
                          FoodCourtSerializer,
                          EventSerializer,
                          PlaceToVisitSerializer)


class Clubs(APIView):
    """Get list of all Clubs"""

    def get(self, request):
        clubs = []
        for club in Club.objects.all().select_related():
            detail = {
                "id": club.id,
                "clubname": club.ClubName,
                "imageurl": club.imageUrl,
                "description": club.description,
                "vice_president": {
                    "id": club.VicePresident.vicepresidentId,
                    "name": club.VicePresident.name,
                    "imageurl": club.VicePresident.image
                },
                "president": {
                    "id": club.President.presidentId,
                    "name": club.President.name,
                    "imageurl": club.President.image
                }
            }
            clubs.append(detail)
        return Response(clubs)


class Socities(ListAPIView):
    """Get List of all Socities"""
    serializer_class = SocietySerializer
    queryset = Society.objects.all()


class Sports(ListAPIView):
    """Get List of all Sports"""
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class Hostels(ListAPIView):
    """Get List of all Hostels"""
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer


class Events(ListAPIView):
    """Get List of all events"""
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class FoodCourts(ListAPIView):
    """Get Lists of all Food Courts"""
    serializer_class = FoodCourtSerializer
    queryset = FoodCourt.objects.all()

class PlacesToVisit(ListAPIView):
    """Get List of all places to visit nearby NIT Hamirpur"""
    queryset = PlaceToVisit.objects.all()
    serializer_class = PlaceToVisitSerializer


class Shops(ListAPIView):
    """Get List of all the Shops"""
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class Departments(ListAPIView):
    """Get Lists of all the Departments"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
