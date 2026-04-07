from django.urls import path
from sales import views

urlpatterns = [
    path('', views.region_list, name='region_list'),
    path('region/<int:region_id>/', views.area_list, name='area_list'),
    # Add similar paths for Territory and Brand...
]