from tkinter import CASCADE
from zoneinfo import available_timezones
from django.db import models
from datetime import datetime
from django.db.models import Sum, Count


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    capacity = models.IntegerField(default=10)

    def __str__(self):
        return self.name + ' - ' + self.description


TYPE_CHOICES = [
    ("public", "public"),
    ("private", "private"),
]


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, default="public")
    date = models.DateField(default="2022-09-01")
    room = 1  # models.OneToOneField(Room, on_delete=models.CASCADE, default=1)
    available_places = models.IntegerField(default=2)

    def __str__(self):

        return self.name + ' - Available spaces: ' + str(self.available_places)

    # def available_places(self):
        # Booking.objects.filter(event__id=self.id).annotate(total=Sum(1)).values('total')[0].get('total')
     #   return self.room.capacity


class Customer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


STATUS_CHOICES = [
    ("idle", "idle"),
    ("reserved", "reserved"),
    ("cancelled", "cancelled"),
]


class Booking(models.Model):
    description = models.CharField(max_length=500)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, default=1)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, default=1)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="idle")

    def __str__(self):
        return str(self.id)

    def check_exists(event, customer):
        resp = False
        if Booking.objects.filter(event__id=event, customer__id=customer)\
            .annotate(total=Count(1))\
                .values('total')[0].get('total') > 0:
            resp = True

        return resp
