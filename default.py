# TODO move this to a config
import logging
from datetime import datetime

from download import download_file
from goes import GoesSatellite
from himawari import HimawariSatellite


def default():
    output_path = '/home/joshua/background.jpg'
    utc_hour = datetime.utcnow().hour
    if utc_hour > 2 and utc_hour < 10:
        url = HimawariSatellite().get_image_url()
        download_file(url, output_path, (832, 852, 832+3840, 852+2160))
    else:
        url = GoesSatellite().get_image_url()
        download_file(url, output_path)
    logging.info(f'Done!')

