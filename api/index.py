import os
import sys
from pathlib import Path

# Add the project root to sys.path so Django can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configure Django settings before any imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

# Setup Django
import django
django.setup()

# Import WSGI application after Django setup
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
app = get_wsgi_application()

# For Vercel: export the WSGI application
application = app

