from django.contrib import admin
from .models import Booking, Room, Event, Customer

admin.site.register(Room)
admin.site.register(Event)
admin.site.register(Customer)
admin.site.register(Booking)
