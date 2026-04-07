import os
from pathlib import Path
from django.core.asgi import get_asgi_application

# Automatically find the folder name
PROJECT_NAME = Path(__file__).resolve().parent.name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')

application = get_asgi_application()