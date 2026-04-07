import random
from django.core.management.base import BaseCommand
from sales.models import Region, Area, Territory, Brand


class Command(BaseCommand):
    help = 'Populates the database with dummy medical sales data'

    def handle(self, *args, **kwargs):
        # 1. Create Regions
        regions_names = ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi', 'Khulna']
        regions = [Region.objects.get_or_create(name=name)[0] for name in regions_names]

        # 2. Create Areas (assigned to random regions)
        for i in range(1, 21):
            Area.objects.create(
                name=f"Area Code {100 + i}",
                region=random.choice(regions)
            )

        # 3. Create Brands (Medical Products)
        med_names = ['Napa', 'Ace', 'Seclo', 'Sergel', 'Fexo', 'Maxpro', 'Alatrol']
        for i in range(1, 26):
            Brand.objects.create(name=f"{random.choice(med_names)} {random.randint(10, 500)}mg")

        self.stdout.write(self.style.SUCCESS('Successfully added 100+ dummy records!'))