from entities.book import Book
from entities.library import Library
from utils.file_utils import DataManager


def read_input_file(input_file: str):
    manager = DataManager("./gitignored_folder")
    save_name = input_file.split("data")[1].replace(".txt", "").replace("/", "")
    data = manager.load_python_obj(save_name)

    if data is None:

        with open(input_file) as f:
            # Read line 1
            num_books, num_libs, max_days = map(
                lambda x: int(x), f.readline().strip().split(' '))
            book_scores = list(
                map(lambda x: int(x), f.readline().strip().split(' ')))
            books = []
            for idx, elem in enumerate(book_scores):
                books.append(Book(id=idx, score=elem))

            book_scores = {x.id: x._score for x in books}

            libs = []
            for idx in range(num_libs):
                # Read library stats
                n_books_lib, signup_days, amount_of_books_per_day = map(
                    lambda x: int(x), f.readline().strip().split(' '))
                # Read books which are in that particular library
                lib_books = list(
                    map(lambda x: int(x), f.readline().strip().split(' ')))

                new_library = Library(book_ids=lib_books, signup_days=signup_days,
                                      amount_of_books_per_day=amount_of_books_per_day, id=idx)

                new_library.scores_sum = sum([book_scores[book_id] for book_id in lib_books])
                libs.append(new_library)

        manager.save_python_obj((num_books, num_libs, max_days, books, libs), save_name)

        return num_books, num_libs, max_days, books, libs

    else:

        return data
