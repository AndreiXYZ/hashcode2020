
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


    def initial_ordering(self):
        return np.random.shuffle(self.libraries)

    def do_solution(self):


        while not self.finished():

            old_state = self.datamanager.personal_deepcopy(self.libraries)





