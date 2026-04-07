from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),  # This looks at your app

    # This line is the magic fix for the 'login' error:
    path('accounts/', include('django.contrib.auth.urls')),
]