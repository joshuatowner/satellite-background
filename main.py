import argparse
import logging
import sys

from default import default


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    args = parser.parse_args()
    default(output_path=args.output)


if __name__ == '__main__':
    main()

