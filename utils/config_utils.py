import argparse


def parse() -> argparse.Namespace:
    """ does argument parsing """

    parser = argparse.ArgumentParser()

    parser.add_argument('--example', default=1000, type=int, help='evaluate every x batches')

    return parser.parse_args()