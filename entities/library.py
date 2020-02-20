from entities.book import Book
from typing import List


class Library:
    def __init__(
            self,
            book_ids: List[int],
            signup_days: int,
            amount_of_books_per_day: int,
            id: int):
        self.id = id
        self.book_ids: List[int] = book_ids
        self.signup_days = signup_days
        self.amount_of_books_per_day = amount_of_books_per_day
        self.scores_sum = 0

    def __repr__(self):
        return 'ID={} Book Ids={} Signup days={} Num. books per day={}'.format(
            self.id, self.book_ids, self.signup_days, self.amount_of_books_per_day
        )
