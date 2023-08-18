import argparse
import logging
import sys

from default import default
from util.desktop_environment import get_desktop_environment
from util.wallpaper import set_wallpaper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-b', '--background', action='store_true')
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    args = parser.parse_args()
    default(output_path=args.output)
    print(get_desktop_environment())
    if args.background:
        set_wallpaper(args.output, True)


if __name__ == '__main__':
    main()
