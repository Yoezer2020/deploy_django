import os
import django
from django.core.wsgi import get_wsgi_application

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dzongkha_nextword.settings')
django.setup()

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line()
