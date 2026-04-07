from django.db import models

# 1. Define Region first
class Region(models.Model):
    name = models.CharField(max_length=100)

# 2. Then Area (linked to Region)
class Area(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)

# 3. Then Territory (linked to Area)
class Territory(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)

# 4. Then Brand (linked to Territory)
class Brand(models.Model):
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sales_value = models.DecimalField(max_digits=12, decimal_places=2)
    last_3_months_data = models.JSONField()
    special_allocation = models.TextField(blank=True)
    remarks = models.TextField(blank=True)