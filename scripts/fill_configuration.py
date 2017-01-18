import sys
import os

dirname = os.path.dirname(__file__)
publicdb_path = os.path.join(dirname, '..')
sys.path.append(publicdb_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_publicdb.settings'

import django
django.setup()

from django_publicdb.inforecords.models import (Configuration,
                                                Summary, Station)
from datetime import datetime
from sapphire.api import Station as APIStation
from sapphire.transformations.clock import gps_to_datetime

STATION = 502

if __name__ == '__main__':
    gps_locations = APIStation(STATION).gps_locations
    for gps in gps_locations:    
        print "item = ", gps
        date = gps_to_datetime(gps['timestamp'])
        station = Station.objects.get(number=STATION)
        summary, _ = Summary.objects.get_or_create(station=station, date=date)
        #summary.save()

        # "default" config
        configs = Configuration.objects.filter(source__station=station)
        first = configs[0]

        field = dict((key, value) for key, value in first.__dict__.iteritems() 
                        if not callable(value) and not key.startswith('_'))   
        
        field.pop('source_id', None)
        field.pop('id', None)
        
        field['timestamp'] = gps_to_datetime(gps['timestamp'])
        field['gps_latitude'] = gps['latitude']
        field['gps_longitude'] = gps['longitude']
        field['gps_altitude'] = gps['altitude'] 
        conf = Configuration.objects.update_or_create(source=summary,defaults=field)
