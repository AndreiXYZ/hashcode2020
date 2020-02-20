import random
import numpy as np

from utils.file_utils import DataManager


class StijnYouri:

    def __init__(self, libraries, books, max_days):
        self.max_days = max_days
        self.books = books
        self.libraries = libraries
        self.initial_ordering()
        self.datamanager = DataManager(".")
        self.finished = False

    def initial_ordering(self):
        return np.random.shuffle(self.libraries)

    def do_solution(self):
        while not self.finished:
            old_state = self.datamanager.personal_deepcopy(self.libraries)

    def simulate_stuff(self, ranking):
        total_score = 0
        ranking = self.libraries
        pool_of_book = {x.id: x._score for x in self.books}
        for day in range(self.max_days):
            available_libraries = self.get_available_libraries(day, ranking)
            if len(available_libraries) == 0:
                pass
            temp_score, pool_of_book = self.calc_stuff(pool_of_book, available_libraries)
            total_score+=temp_score
        return total_score


    def calc_stuff(self, pool_of_book, available_libraries):
        temp_score = 0
        for lib in available_libraries:
            amount_of_books_per_day = lib._amount_of_books_per_day
            books_submitted = 0
            for book_id in lib._book_ids:
                if book_id in pool_of_book.keys():
                    temp_score+=pool_of_book[book_id]
                    books_submitted+=1
                    del pool_of_book[book_id]
                    if books_submitted == amount_of_books_per_day:
                        break

        return temp_score, pool_of_book

    def get_available_libraries(self, day, ranking):
        total = 0
        available_libraries = []
        for library in ranking:
            total += library._signup_days
            if day > total:
                available_libraries.append(library)
            else:
                break
        return available_libraries


