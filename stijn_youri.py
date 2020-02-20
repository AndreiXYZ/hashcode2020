import random
from typing import List

import numpy as np

from entities.library import Library
from utils.file_utils import DataManager


class StijnYouri:

    def __init__(self, libraries, books, max_days):
        self.max_days = max_days
        self.books = np.array(books)
        self.libraries = np.array(libraries)
        self.datamanager = DataManager(".")
        self.state = np.array(range(len(self.libraries)))
        self.length_state = len(self.state)
        self.initial_ordering()
        self.patience = 100
        self.score_history = []
        self.accept_worse_order_prob = 1

    def initial_ordering(self, method="greedy_div_time_amount"):
        print("initial ordering")
        if method=="random":
            # random for now
            np.random.shuffle(self.state)

        elif method == "greedy":
            self.state = np.argsort([-1*lib.scores_sum for lib in self.libraries])

        elif method == "greedy_div_time":
            self.state = np.argsort([-1*(lib.scores_sum/lib.signup_days) for lib in self.libraries])

        elif method == "greedy_div_time_amount":
            self.state = np.argsort([-1*((lib.scores_sum*lib.amount_of_books_per_day)/lib.signup_days) for lib in self.libraries])




    def do_solution(self):

        try:

            print("starting run")
            # initial evaluation
            score = self.simulate_stuff(self.get_cutoff())

            timestep = 0

            # exit condition
            while not self.finished():

                timestep += 1

                print(
                    f"\rtime {timestep}, score {score}, patience {self.patience}", end='')

                # save for now
                old_state = self.datamanager.personal_deepcopy(self.state)

                # change state
                self.do_flip()

                # evaluate new state
                new_score = self.simulate_stuff(self.get_cutoff())

                # change is accepted if better or sometimes with random probability
                if new_score >= score or (random.random() - self.accept_worse_order_prob) > 0:

                    # move forward
                    del old_state
                    self.score_history.append(new_score)
                    score = new_score

                    # reset patience
                    self.patience = 100
                else:
                    # rejected forward
                    self.state = old_state
                    self.patience -= 1

                if self.patience == 0:
                    print("\n\nexit because ran out of patience")
                    return self.get_cutoff()

        except KeyboardInterrupt:
            print("\n\nKilled, returning current solution")
            # todo: are books sorted as well?
            cutoff = self.get_cutoff()
            simulation_score = self.simulate_stuff(cutoff)

            return cutoff, self.lib_books

    def do_flip(self, method="random_multiple"):
        # flips two random indices, for now
        if method == "random_once":
            two_indices = np.array(
                [random.randint(0, self.length_state - 1) for _ in range(2)])
            while two_indices[0] == two_indices[1]:
                two_indices[0] = random.randint(0, self.length_state - 1)
            self.state[two_indices] = self.state[np.flip(two_indices)]
        elif method == "random_multiple":
            for x in range(5):
                self.do_flip(method="random_once")
        elif method == "skewed_for_total_score":

            pass  # todo

        else:
            raise ValueError(method)

    def finished(self):
        # for now
        return False

    def get_cutoff(self) -> List[Library]:
        # find how many libraries can fit

        order = self.libraries[self.state]
        days_left = self.max_days
        index = 0
        while days_left > 0 and index < len(order):
            lib = order[index]
            lib: Library
            days_left -= lib.signup_days
            index += 1
        return order[:index - 1]

    def simulate_stuff(self, ranking):
        total_score = 0
        self.ranking = {x.id: x for x in ranking}
        self.pool_of_book = {x.id: x._score for x in self.books}
        self.depleted_libraries = {x.id: False for x in ranking}
        self.scanned_books = {x.id: False for x in self.books}
        self.lib_books = []
        for lib in self.libraries:
            self.lib_books.append([])

        for day in range(self.max_days):
            available_library_ids = self.get_available_library_ids(day)
            if len(available_library_ids) == 0:
                continue

            temp_score = self.calc_stuff(available_library_ids)
            total_score += temp_score
        return total_score

    def calc_stuff(self, available_library_ids: List[Library]):
        temp_score = 0
        for library_id in available_library_ids:
            if self.depleted_libraries[library_id]:
                continue

            amount_of_books_per_day = self.ranking[library_id].amount_of_books_per_day
            books_submitted = 0
            for book_id in self.ranking[library_id].book_ids:
                if self.scanned_books[book_id]:
                    continue

                self.lib_books[library_id].append(book_id)
                temp_score += self.pool_of_book[book_id]
                books_submitted += 1
                self.scanned_books[book_id] = True
                if books_submitted == amount_of_books_per_day:
                    break

            if books_submitted == 0:
                self.depleted_libraries[library_id] = True

        return temp_score

    def get_available_library_ids(self, day):
        total = 0
        available_library_ids = []
        for library_id, library in self.ranking.items():
            total += library.signup_days
            if day > total:
                available_library_ids.append(library_id)
            else:
                break

        return available_library_ids
