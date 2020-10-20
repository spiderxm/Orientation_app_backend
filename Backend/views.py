from rest_framework.views import APIView
from .models import Club
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Society, Sport
from .serializers import SocietySerializer, SportSerializer

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



def Hostels(request):
    """Get List of all Hostels"""
    pass


def Events(request):
    """Get List of all events"""
    pass


def FoodCourts(request):
    """Get Lists of all Food Courts"""
    pass


def PlacesToVisit(request):
    """Get List of all places to visit nearby NIT Hamirpur"""


def Shops(request):
    pass


def Departments(request):
    pass
