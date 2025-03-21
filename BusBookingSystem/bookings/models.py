from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    bus_number = models.CharField(max_length=10)
    route = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.bus_number} - {self.route}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    payment_status = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Booking by {self.user.username} for Bus {self.bus.bus_number}"
