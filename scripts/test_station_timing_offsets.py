import os
import sys

dirname = os.path.dirname(__file__)
publicdb_path = os.path.join(dirname, '..')
sys.path.append(publicdb_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_publicdb.settings'

import django
django.setup()

import django_publicdb.histograms as hg
import django_publicdb.inforecords as ir

from datetime import datetime
from dateutil import rrule
from sapphire.transformations.clock import gps_to_datetime, datetime_to_gps
import numpy as np
import tables

REF = 501
STATION = 502
INPUTFILE = 'dt_ref%d_%d.h5' % (REF, STATION)


def do():
    to = hg.esd.StationTimingOffsetsESD([501, 502])
    offsets = to.determine_station_timing_offsets(502, 501)
    print offsets
    np.save('offsets_publicdb_%d_ref%d.npy' % (STATION, REF), offsets)

if __name__ == '__main__':
    station = ir.models.Station.objects.get(number=501)
