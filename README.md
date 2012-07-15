#Django-Skeleton

###Here be dragons! 

This is a base skeleton [Django](https://www.djangoproject.com/) project
configured with the following libraries in a pip requirements.txt file:

* django
* south
* django-registration
* django-debug-toolbar
* django-extensions
* django-storages
* django-templates
* django-registration-templates

Ideally, this project can be used in conjunction with [django-vagrant](http://github.com/ryankanno/django-vagrant/) 
as there's a custom fabfile so you don't have to pollute your own development
machine.

Enjoy!


##Features 

* Custom fabfile.py for use with [django-vagrant](http://github.com/ryankanno/django-vagrant/)
* HTML templates via [django-templates](http://github.com/ryankanno/django-templates/)
* Registration templates via [django-registration-templates](http://github.com/ryankanno/django-registration-templates)


##Prerequisites

If you don't have [django-vagrant](http://github.com/ryankanno/django-vagrant/)
installed, please mozy on over and install it.  You'll thank me later. (Maybe
:D)

You'll also probably need Python and Fabric installed.  At the time of this
writing, I tested this with Python 2.7.3 and Fabric 1.4.3


##Install

* `git clone http://github.com/ryankanno/django-skeleton` # clone the repo

Assuming you have the [django-vagrant](http://github.com/ryankanno/django-vagrant/)
up and running, we can use fabric to install this skeleton to the Vagrant
instance.

* `fab production master setup` 
* `fab production configure_www:file=etc/nginx.conf.in`
* `fab production configure_uwsgi:file=etc/uwsgi.conf.in`


##Deploy

Once you've made changes to the skeleton project, run the following

* `fab production master deploy` # deploy the codes
* `fab production app:restart`     # restart the uwsgi server

Point your browser at `http://88.88.88.88`

Win.

##Supported Fabric Commands

###Redeploy codes
* `fab production master deploy` # deploy the codes

or

* `fab production master deploy:update_requirements=True` # deploy the codes with requirements

###Web server
* `fab production configure_www:file=etc/nginx.conf.in` # Update conf file - uses relative path from repo root
* `fab production www:[start|stop|restart]` # pass through to init.d commands

###App server
* `fab production configure_uwsgi:file=etc/uwsgi.conf.in` # Update conf file - uses relative path from repo root
* `fab production app:[start|stop|restart]` # pass through to init.d commands

###Maintenance pages
* `fab production maintenance_up` # Will prompt for a reason
* `fab production maintenance_down` # Removes the maintenance page

###Execute manage.py commands
* `fab production manage:syncdb` # Run syncdb
* `fab production manage:collectstatic` # Run collectstatic
