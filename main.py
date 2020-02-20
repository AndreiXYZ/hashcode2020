import os

from stijn_youri import StijnYouri
from utils.config_utils import *
from utils.input_utils import *
from utils.output_utils import *
from entities.book import Book
import argparse
from entities.book import Book
from entities.library import Library


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', type=str, default="./data/c_incunabula.txt")
    parser.add_argument('--method', type=str, default="stijn_youri")
    args = parser.parse_args()



    num_books, num_libs, max_days, books, libs = read_input_file(args.input_file)


    # optional

    if args.method == "stijn_youri":
        solution = StijnYouri(libs, books, max_days).do_solution()



    # read


    # calculate

    libraries_to_signup = len(libs)  # TODO Calculate
    save_result(
        libs,
        libraries_to_signup,
        [library.id for library in libs],
        [library.book_ids for library in libs],
        args.input_file)

# output
