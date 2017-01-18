import os
import sys

dirname = os.path.dirname(__file__)
publicdb_path = os.path.join(dirname, '..')
sys.path.append(publicdb_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_publicdb.settings'

import django
django.setup()

import django_publicdb.histograms as hg

from datetime import datetime
from dateutil import rrule
from sapphire.transformations.clock import gps_to_datetime, datetime_to_gps
import tables

REF = 501
STATION = 502
INPUTFILE = 'dt_ref%d_%d.h5' % (REF, STATION)



if __name__ == '__main__':

    with tables.open_file(INPUTFILE, 'r') as h5in:
        dt_table = h5in.get_node('/s%d' % STATION)
	recarray = dt_table.read()

	start = gps_to_datetime(recarray[0]['timestamp']).date()
	end = gps_to_datetime(recarray[-1]['timestamp']).date()

	for date in rrule.rrule(rrule.DAILY, dtstart=start, until=end):
            print date,
	    first_ts = datetime_to_gps(date)
	    last_ts = int(first_ts + 24 * 3600)
	    recarray = dt_table.read_where('(timestamp >= first_ts) & (timestamp < last_ts)')
	    print len(recarray)
	    ets = recarray['ext_timestamp']
	    dt = recarray['delta']
	    if len(dt) < 100: continue
	    filepath = hg.esd.get_or_create_esd_data_path(date)
	    with tables.open_file(filepath, 'a') as data:
	        hg.esd.store_time_deltas(data, REF, STATION, ets, dt)

