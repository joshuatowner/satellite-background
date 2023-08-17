import logging
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from satellite import Satellite


class HimawariSatellite(Satellite):
    landing_url = "https://rammb.cira.colostate.edu/ramsdis/online/archive_hi_res.asp?data_folder=himawari-8/full_disk_ahi_true_color&width=800&height=800"

    def get_image_url(self):
        req = requests.get(self.landing_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        element = soup.find('a', href=True, text='Hi-Res Image')
        if element is None:
            raise Exception('Unable to find link to GOES Image')
        url = urljoin(self.landing_url, element.get('href'))
        logging.info(f'Found Himawari URL {url}')
        return url
