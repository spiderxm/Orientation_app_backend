from django.db import models
import uuid


class PresidentClub(models.Model):
    presidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)


class VicePresidentClub(models.Model):
    vicepresidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)


class PresidentSociety(models.Model):
    presidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)


class VicePresidentSociety(models.Model):
    vicepresidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)


class Club(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    ClubName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    President = models.ForeignKey(PresidentClub, db_column="presidentId", on_delete=models.DO_NOTHING)
    VicePresident = models.ForeignKey(VicePresidentClub, db_column="vicepresidentId", on_delete=models.DO_NOTHING)


class Society(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    SocietyName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    President = models.ForeignKey(PresidentSociety, db_column="presidentId", on_delete=models.DO_NOTHING)
    VicePresident = models.ForeignKey(VicePresidentSociety, db_column="vicepresidentId", on_delete=models.DO_NOTHING)


class Sport(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    SportName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class Hostel(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    HostelName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class Event(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    Event = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class FoodCourt(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    Name = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class PlaceToVisit(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    PlaceName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class Shop(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    ShopName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)


class Department(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    DepartmentName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    seats = models.PositiveIntegerField(null=False)
