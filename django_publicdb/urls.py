from django.conf.urls.defaults import *
from inforecords.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_publicdb/', include('django_publicdb.foo.urls')),

    (r'^$', 'django.views.generic.simple.redirect_to',
     {'url': '/django/show/stations', 'permanent': False}),

    (r'^update_check/$', 'django_publicdb.histograms.views.update_check'),
    (r'^update_histograms/$', 'django_publicdb.histograms.views.update_histograms'),

    (r'^gateway/$', 'django_publicdb.histograms.amfgateway.publicgateway'),

    (r'^show/', include('django_publicdb.status_display.urls')),

    (r'^config/nagios$', create_nagios_config),

    (r'^keys/(?P<host>\w+)/$', 'django_publicdb.inforecords.views.keys'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)