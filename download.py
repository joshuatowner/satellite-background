import logging
import shutil
import tempfile
import urllib

from PIL import Image


def crop(file, dimensions):
    im = Image.open(file)
    im1 = im.crop(dimensions)
    im1.save(file)


def download_file(url, output_path, crop_options=None):
    with tempfile.NamedTemporaryFile(suffix='.jpg') as temp:
        temp_path = temp.name
        logging.info(f'Downloading {url} to {temp_path}')
        urllib.request.urlretrieve(url, temp_path)

        if crop_options is not None:
            crop(temp_path, crop_options)

        logging.info(f'Exporting to {output_path}')
        shutil.copy(temp_path, output_path)
