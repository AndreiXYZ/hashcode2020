import os

from stijn_youri import StijnYouri
from utils.config_utils import *
from utils.input_utils import *
from utils.output_utils import *
from entities.book import Book
import argparse
from entities.book import Book
from entities.library import Library
from andrei_max_books import solution

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', type=str, default="./data/c_incunabula.txt")
    parser.add_argument('--method', type=str, default="stijn_youri")
    args = parser.parse_args()

    num_books, num_libs, max_days, books, libs = read_input_file(args.input_file)


    # optional

    if args.method == "stijn_youri":
        libraries_to_signup, library_books = StijnYouri(libs, books, max_days).do_solution()

    if args.method == 'andrei_maxbooks':
        libraries_to_signup, library_books = solution(books, libs, max_days)
    # read

    # calculate
    save_result(
        libs,
        len(libraries_to_signup),
        libraries_to_signup,
        library_books,
        args.input_file)

# output
