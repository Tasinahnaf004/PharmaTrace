from django.shortcuts import render, get_object_or_404
from .models import Region, Area

def region_list(request):
    regions = Region.objects.prefetch_related('areas').all()
    return render(request, 'sales/regions.html', {'regions': regions})

def area_detail(request, area_id):
    area = get_object_or_404(Area, id=area_id)
    # Get the sales records for this specific area
    sales = area.sales_records.all().order_by('-id')[:3]
    return render(request, 'sales/area_detail.html', {'area': area, 'sales': sales})