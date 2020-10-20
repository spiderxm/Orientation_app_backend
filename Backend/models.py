from django.db import models
import uuid


class Club(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class Society(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class Sport(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class Hostel(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class Event(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class FoodCourt(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class PlaceToVisit(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


class Shop(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True)


def Department(request):
    id = models.CharField(default=uuid.uuid4, primary_key=True)

