from rest_framework.views import APIView
from .models import Club
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Society, Sport, Shop, Hostel, Department, PlaceToVisit, UserUpload, Event, FoodCourt
from .serializers import (SocietySerializer,
                          SportSerializer,
                          ShopSerializer,
                          DepartmentSerializer,
                          HostelSerializer,
                          FoodCourtSerializer,
                          EventSerializer,
                          UserUploadSerializer,
                          PlaceToVisitSerializer)
from rest_framework import status


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


class Posts(ListAPIView):
    """Get List of all the Posts"""
    queryset = UserUpload.objects.all()
    serializer_class = UserUploadSerializer

    def get_queryset(self):
        return UserUpload.objects.all().order_by("-timeOfUpload")

class UploadImage(APIView):
    """Upload Image of user"""

    def post(self, request):
        try:
            data = request.data
            print(data)
            userId = data['userId']
            imageUrl = data['imageUrl']
            userName = data['userName']
            description = data['description']
            email = data['email']
            latitude = data['latitude']
            longitude = data['longitude']
            post = UserUpload.objects.create(
                userId=userId,
                userName=userName,
                description=description,
                userEmail=email,
                imageUrl=imageUrl,
                latitude=latitude,
                longitude=longitude
            )
            post.save()
            return Response({
                "message": "Post created successfully",
                "post": {
                    "postId": post.id,
                    "userId": post.userId,
                    "imageUrl": post.imageUrl,
                    "userName": post.userName,
                    "timeOfUpload": post.timeOfUpload,
                    "userEmail": post.userEmail
                }
            }, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            """Return Error when post is not created"""
            return Response({
                "message": "error",
                "detail": "Please try again later."
            }, status=status.HTTP_400_BAD_REQUEST)
