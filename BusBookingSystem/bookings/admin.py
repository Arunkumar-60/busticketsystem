from django.contrib import admin
from .models import Bus, Booking

# Registering the Bus model in the Django admin panel
admin.site.register(Bus)

# Registering the Booking model in the Django admin panel
admin.site.register(Booking)
