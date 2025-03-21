import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Bus, Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BusSerializer

def generate_qr_code(data):
    qr = qrcode.QCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer

def book_ticket(request, bus_id, seat_number):
    user = request.user
    bus = get_object_or_404(Bus, id=bus_id)

    # Ensure the seat isn't already booked
    if Booking.objects.filter(bus=bus, seat_number=seat_number).exists():
        return HttpResponse("Seat already booked", status=400)

    booking = Booking.objects.create(
        user=user,
        bus=bus,
        seat_number=seat_number,
        payment_status=True,  # Assume payment is successful
    )

    # Generate QR code
    qr_data = f"Name: {user.username}\nBus: {bus.route}\nSeat: {seat_number}"
    qr_code_image = generate_qr_code(qr_data)
    booking.qr_code.save(f"qr_{booking.id}.png", qr_code_image, save=True)

    return HttpResponse("Booking successful!")


@api_view(['GET'])  # Specify that this view will handle GET requests
def bus_schedule(request):
    buses = Bus.objects.all()  # Get all bus records from the database
    serializer = BusSerializer(buses, many=True)  # Serialize the buses data
    return Response(serializer.data)  # Return serialized data as JSON

