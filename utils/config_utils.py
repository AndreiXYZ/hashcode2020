import argparse


def parse() -> argparse.Namespace:
    """ does argument parsing """

    parser = argparse.ArgumentParser()

    parser.add_argument('--filename', default=None, type=str, help='name of file')

    return parser.parse_args()