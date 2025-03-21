from django.urls import path
from . import views
from .views import bus_schedule  # Import the bus_schedule view


urlpatterns = [
    path('book/<int:bus_id>/<str:seat_number>/', views.book_ticket, name='book_ticket'),
    path('buses/', bus_schedule, name='bus-schedule'),  # Defining the API endpoint
]


