from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='areas')
    def __str__(self):
        return self.name

# --- THIS IS THE NEW PART ---
class SalesRecord(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='sales_records')
    rsm_name = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.area.name} - {self.month}"