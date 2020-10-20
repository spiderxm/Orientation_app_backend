from django.db import models
import uuid


class PresidentClub(models.Model):
    presidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)

    def __str__(self):
        return self.name


class VicePresidentClub(models.Model):
    vicepresidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)

    def __str__(self):
        return self.name


class PresidentSociety(models.Model):
    presidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)

    def __str__(self):
        return self.name


class VicePresidentSociety(models.Model):
    vicepresidentId = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    name = models.TextField(null=False, max_length=256)
    image = models.URLField(null=False)

    def __str__(self):
        return self.name


class Club(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    ClubName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    President = models.ForeignKey(PresidentClub, db_column="presidentId", on_delete=models.DO_NOTHING)
    VicePresident = models.ForeignKey(VicePresidentClub, db_column="vicepresidentId", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ClubName


class Society(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    SocietyName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    President = models.ForeignKey(PresidentSociety, db_column="presidentId", on_delete=models.DO_NOTHING)
    VicePresident = models.ForeignKey(VicePresidentSociety, db_column="vicepresidentId", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.SocietyName


class Sport(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    SportName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)

    def __str__(self):
        return self.SportName


class Hostel(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    HostelName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)

    def __str__(self):
        return self.HostelName


class Event(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    Event = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)

    def __str__(self):
        return self.Event


class FoodCourt(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    Name = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)

    def __str__(self):
        return self.Name


class PlaceToVisit(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    PlaceName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    distance = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return self.PlaceName


class Shop(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    ShopName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)

    def __str__(self):
        return self.ShopName


class Department(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, max_length=256)
    DepartmentName = models.CharField(null=False, max_length=256)
    description = models.TextField(null=False)
    imageUrl = models.URLField(null=False)
    seats = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.DepartmentName
