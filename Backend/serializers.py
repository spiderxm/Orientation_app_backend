from rest_framework import serializers
from .models import Society, VicePresidentSociety, PresidentSociety, Sport


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

