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
        self._book_ids: List[int] = book_ids
        self._signup_days = signup_days
        self._amount_of_books_per_day = amount_of_books_per_day

    def __repr__(self):
        return 'ID={} Book Ids={} Signup days={} Num. books per day={}'.format(
            self.id, self._book_ids, self._signup_days, self._amount_of_books_per_day
        )
