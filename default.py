# TODO move this to a config
import logging
from datetime import datetime

from download import download_file
from goes import GoesSatellite
from himawari import HimawariSatellite


def default(output_path):
    utc_hour = datetime.utcnow().hour
    if utc_hour > 21 or utc_hour < 12:
        url = HimawariSatellite().get_image_url()
        download_file(url, output_path, (832, 852, 832 + 3840, 852 + 2160))
    else:
        url = GoesSatellite().get_image_url()
        download_file(url, output_path, (0, 200, 9216, 5384))
