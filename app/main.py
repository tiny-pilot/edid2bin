#!/usr/bin/env python3

import argparse
import binascii
import logging
import sys

logger = logging.getLogger(__name__)


def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def parse_edid():
    return sys.stdin.read().strip().lower().replace(' ', '').replace('\n', '')


def save_edid(edid, output_path):
    with open(output_path, 'wb') as outfile:
        outfile.write(binascii.unhexlify(edid))


def main(args):
    configure_logging()
    logger.info('Started runnning')
    save_edid(parse_edid(), args.output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Make EDID',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output', required=True)
    main(parser.parse_args())
