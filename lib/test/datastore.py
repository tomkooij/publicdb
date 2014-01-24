import os

from django.conf import settings

from scripts import download_test_datastore
from django_publicdb import inforecords


def setup_test_datastore_directory(datastore_path):

    if not os.path.exists(datastore_path):
        os.makedirs(datastore_path)
    else:
        test_file = os.path.join(datastore_path, "testfile")
        f = open(test_file, 'w')
        f.write("test")
        f.flush()
        f.close()

        f = open(test_file, 'r')
        content = f.read()
        f.close()

        os.remove(test_file)

    settings.DATASTORE_PATH = datastore_path

    settings.ESD_PATH = os.path.join(datastore_path, "esd")

    if not os.path.exists(settings.ESD_PATH):
        os.makedirs(settings.ESD_PATH)


def get_datafile_path(date):
    return os.path.join(settings.DATASTORE_PATH,
                        '%d/%d' % (date.year, date.month),
                        '%d_%d_%d.h5' % (date.year, date.month, date.day))


def download_data_station(station_number, date, get_blobs=False):
    station = inforecords.models.Station.objects.get(number=station_number)

    file = get_datafile_path(date)

    f = download_test_datastore.open_or_create_file(settings.DATASTORE_PATH,
                                                    date)

    download_test_datastore.download_and_store_station_data(f, station,
                                                            date, get_blobs)

    f.close()

    return file
