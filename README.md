#Django-Skeleton

###Here be dragons! 

This is a base skeleton [Django](https://www.djangoproject.com/) project
configured with the following libraries in a pip requirements.txt file:

* South==0.7.5
* Django==1.4.0

* -e hg+http://bitbucket.org/ubernostrum/django-registration/#egg=registration
* -e git+https://github.com/django-debug-toolbar/django-debug-toolbar.git#egg=django-debug-toolbar
* -e git+https://github.com/django-extensions/django-extensions.git#egg=django-extensions
* -e hg+https://bitbucket.org/david/django-storages/#egg=django-storages

* -e git+https://github.com/ryankanno/django-templates.git#egg=django-templates
* -e git+https://github.com/ryankanno/django-registration-templates.git#egg=django-registration-templates

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


###Deploy

Once you've made changes to the skeleton project, run the following

* `fab production master deploy`

Point your browser at `http://88.88.88.88`

Win.
