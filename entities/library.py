from entities.book import Book
from typing import List


class Library:
    def __init__(
            self,
            book_ids: List[int],
            signup_days: int,
            amount_of_books_per_day: int):
        self.id = 0
        self._book_ids: List[int] = book_ids
        self._signup_days = signup_days
        self._amount_of_books_per_day = amount_of_books_per_day
