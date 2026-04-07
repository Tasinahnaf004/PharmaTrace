from django.contrib import admin
from .models import Region, Area, SalesRecord

# We only register what we actually created in models.py
admin.site.register(Region)
admin.site.register(Area)
admin.site.register(SalesRecord)