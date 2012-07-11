#Django-Skeleton

Here be dragons! 

This is a skeleton Django 1.4 project.

Enjoy.

##Features 

* Custom fabfile
* Templates via [django-templates](http://github.com/ryankanno/django-templates/)

##Prerequisites

If you don't have [django-vagrant](http://github.com/ryankanno/django-vagrant/)
installed, mozy on over on download it.  You'll thank me later.

##Install

* `git clone http://github.com/ryankanno/django-skeleton`
* `fab production master setup`
* `fab production configure_www:file=etc/nginx.conf.in`
* `fab production configure_uwsgi:file=etc/uwsgi.conf.in`

###Deploy

Once you've made changes to the project, run the following

* `fab production master deploy`

Point your browser at `http://88.88.88.88`

Win!
