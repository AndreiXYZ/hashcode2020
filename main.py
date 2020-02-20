from utils.config_utils import *
from utils.input_utils import *
from utils.output_utils import *
from utils.file_utils import *
import argparse
from entities.book import Book
from entities.library import Library



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', type=str)
    args = parser.parse_args()

    with open(args.input_file) as f:
        # Read line 1
        num_books, num_libs, max_days = map(lambda x: int(x), f.readline().strip().split(' '))
        book_scores = list(map(lambda x: int(x), f.readline().strip().split(' ')))
        books = []
        for idx,elem in enumerate(book_scores):
            books.append(Book(id=idx, score=elem))
        
        libs = []
        for idx in range(num_libs):
            # Read library stats
            n_books_lib, signup_days, amount_of_books_per_day = map(lambda x: int(x), f.readline().strip().split(' '))
            # Read books which are in that particular library
            lib_books = list(map(lambda x: int(x), f.readline().strip().split(' ')))
            libs.append(Library(book_ids=lib_books, signup_days=signup_days, 
                                amount_of_books_per_day=amount_of_books_per_day, id=idx))

    
    # optional
    # read
    # calculate

    # output
