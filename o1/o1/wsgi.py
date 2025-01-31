import os
import sys
from django.core.wsgi import get_wsgi_application
# Add the project directory to the Python path
sys.path.append('E:/Django/1/o1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'o1.settings')

application = get_wsgi_application()
