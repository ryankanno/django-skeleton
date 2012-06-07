import os.path
import sys

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..'))
sys.path.insert(0, PROJECT_ROOT)

from django.core.management import setup_environ
from sample_project import settings 

setup_environ(settings)

DOMAIN = "test.com"
ADMIN_USERNAME = "test"
ADMIN_PASSWORD = "test"


def setup():

    # Create & drop database tables
    #from lib.django_utilities.utilities.management.commands import drop_create
    #drop_create.Command().handle_noargs(interactive=False)

    # Sync database tables
    from django.core.management import call_command 
    call_command('syncdb') 

    # Create admin account
    from django.contrib.auth.models import User
    admin = User.objects.create_superuser(ADMIN_USERNAME, "test@test.com", ADMIN_PASSWORD)
    admin.first_name = 'Test Admin'
    admin.save()

    from django.contrib.sites.models import Site
    site = Site.objects.get(id=1)
    site.domain = DOMAIN
    site.save()


def main(argv):
    setup()

if __name__ == "__main__":
    main(sys.argv[1:])
