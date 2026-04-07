import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'med_project.settings')
django.setup()

from sales.models import Region, Area, Territory, Brand


def populate():
    # Lists of dummy medical data
    regions_list = ['Dhaka', 'Chittagong', 'Sylhet', 'Khulna', 'Rajshahi']
    brands_list = ['Napa', 'Ace', 'Seclo', 'Sergel', 'Fexo', 'Maxpro', 'Osartil']

    print("Deleting old data...")
    Region.objects.all().delete()

    print("Creating 100+ dummy records...")
    for r_name in regions_list:
        region = Region.objects.create(name=r_name)

        # Create 3 Areas for each Region
        for i in range(1, 4):
            area_code = f"{r_name[:3].upper()}-AR-{i:02d}"
            area = Area.objects.create(region=region, code=area_code)

            # Create 2 Territories for each Area
            for j in range(1, 3):
                t_code = f"{area_code}-TR-{j:02d}"
                territory = Territory.objects.create(area=area, code=t_code)

                # Create random Brands for each Territory
                selected_brands = random.sample(brands_list, 3)
                for b_name in selected_brands:
                    sales = random.randint(50000, 500000)
                    Brand.objects.create(
                        territory=territory,
                        name=b_name,
                        sales_value=sales,
                        last_3_months_data={
                            "Jan": random.randint(40000, 450000),
                            "Feb": random.randint(40000, 450000),
                            "Mar": sales
                        },
                        special_allocation=f"Extra {random.randint(5, 20)}% for Eid Season",
                        remarks="Performance is stable."
                    )

    print("Done! 100+ items added successfully.")


if __name__ == '__main__':
    populate()