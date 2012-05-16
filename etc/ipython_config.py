
def load_django_models():
    try:
        from django.db.models.loading import get_models
        for m in get_models():
            ip.ex("from %s import %s" % (m.__module__, m.__name__))
    except ImportError:
        print "Could not find Django. Sadface. D:"

def main():
    load_django_models()
