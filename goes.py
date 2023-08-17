import logging

import requests
from bs4 import BeautifulSoup

from satellite import Satellite


class GoesSatellite(Satellite):
    landing_url = "https://www.star.nesdis.noaa.gov/goes/conus.php?sat=G16"

    def get_image_url(self):
        req = requests.get(self.landing_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        element = soup.find('a', href=True, text='10000 x 6000 px')
        if element is None:
            raise Exception('Unable to find link to GOES Image')
        url = element.get('href')
        logging.info(f'Found GOES URL {url}')
        return url
