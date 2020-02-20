import os
from typing import List

from entities.book import Book
from entities.library import Library

from utils.file_utils import DataManager

data_manager = DataManager(directory='results')


def save_result(
        libraries: List[Library],
        libraries_to_signup: int,
        library_ids_order: List[int],
        book_ids_per_library: List[List[int]],
        input_file_name: str):

    output_str = f'{libraries_to_signup}\n'

    for library_id in library_ids_order:
        books_to_scan = len(libraries[library_id].book_ids)
        output_str += f'{libraries[library_id].id} {books_to_scan}\n'

        for book_id in libraries[library_id].book_ids:
            output_str += f'{str(book_id)} '

        output_str += '\n'

    _, filename = os.path.split(input_file_name)
    data_manager.write_to_file(f'out-{filename}', output_str)
