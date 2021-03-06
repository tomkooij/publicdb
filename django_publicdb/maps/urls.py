from django.conf.urls import patterns

urlpatterns = patterns('django_publicdb.maps.views',
    (r'^$', 'stations_on_map'),
    (r'^(?P<station_number>\d+)/$', 'station_on_map'),
    (r'^(?P<country>[a-zA-Z \-]+)/$', 'stations_on_map'),
    (r'^(?P<country>[a-zA-Z \-]+)/(?P<cluster>[a-zA-Z \-]+)/$', 'stations_on_map'),
    (r'^(?P<country>[a-zA-Z \-]+)/(?P<cluster>[a-zA-Z \-]+)/(?P<subcluster>[a-zA-Z \-]+)/$', 'stations_on_map'),
)
