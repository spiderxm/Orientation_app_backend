from rest_framework import serializers
from .models import Society, VicePresidentSociety, PresidentSociety, Sport, Hostel, Shop, PlaceToVisit, Department, \
    Event, \
    FoodCourt, UserUpload


class UserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpload
        fields = '__all__'


class FoodCourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCourt
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PlaceToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToVisit
        fields = '__all__'


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class VicePresidentSocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = VicePresidentSociety
        fields = '__all__'


class PresidentSocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = PresidentSociety
        fields = '__all__'


class SocietySerializer(serializers.ModelSerializer):
    VicePresident = VicePresidentSocietySerializer()
    President = PresidentSocietySerializer()

    class Meta:
        model = Society
        fields = ['id', 'description', 'SocietyName', 'imageUrl', 'President', 'VicePresident']
