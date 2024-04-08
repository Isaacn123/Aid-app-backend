import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')
django.setup()

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())