from rest_framework.views import APIView
from .models import Club
from rest_framework.response import Response
import json


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


def Socities(request):
    """Get List of all Socities"""
    pass


def Sports(request):
    """Get List of all Sports"""
    pass


def Hostels(request):
    """Get List of all Hostels"""
    pass


def Events(request):
    """Get List of all events"""
    pass


def FoodCourts(request):
    pass


def PlacesToVisit(request):
    pass


def Shops(request):
    pass


def Departments(request):
    pass
