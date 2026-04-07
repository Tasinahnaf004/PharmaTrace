from django.shortcuts import render, get_object_or_404
from .models import Region, Area

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'regions.html', {'regions': regions})

def area_list(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    areas = Area.objects.filter(region=region)
    return render(request, 'areas.html', {'areas': areas, 'region': region})