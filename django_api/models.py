from tkinter import CASCADE
from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    capacity = models.PositiveIntegerField(default=0)

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
    date = models.DateField()
    room = models.OneToOneField(Room, on_delete=models.CASCADE, default=1)
    available_places = "100000"

    def __str__(self):
        return self.name + ' - ' + self.available_places


class Customer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


STATUS_CHOICES = [
    ("reserved", "reserved"),
    ("cancelled", "cancelled"),
]


class Booking(models.Model):
    description = models.CharField(max_length=500)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, default=1)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, default=1)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="reserved")

    def __str__(self):
        return str(self.id)
