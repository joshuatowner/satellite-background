import logging
import sys

from default import default


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    default()


if __name__ == '__main__':
    main()

