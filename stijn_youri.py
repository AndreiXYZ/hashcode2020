import random
from typing import List

import numpy as np

from entities.library import Library
from utils.file_utils import DataManager


class StijnYouri:

    def __init__(self, libraries, books, max_days):
        self.max_days = max_days
        self.books = books
        self.libraries = np.array(libraries)
        self.datamanager = DataManager(".")
        self.state = np.array(range(len(self.libraries)))
        self.length_state = len(self.state)
        self.initial_ordering()
        self.patience = 100
        self.score_history = []
        self.accept_worse_order_prob = 0.95

    def get_score(self, libraries):
        return random.random() # todo: youri

    def initial_ordering(self):
        # random for now
        return np.random.shuffle(self.state)

    def do_solution(self):

        # initial evaluation
        score = self.get_score(self.get_cutoff())

        timestep = 0

        # exit condition
        while not self.finished():

            timestep += 1

            # print(f"\rtime {timestep}, score {score}, patience {self.patience}", end='')

            # save for now
            old_state = self.datamanager.personal_deepcopy(self.state)

            # change state
            self.do_flip()

            # evaluate new state
            new_score = self.get_score(self.get_cutoff())

            # change is accepted if better or sometimes with random probability
            if new_score >= score or (random.random() + self.accept_worse_order_prob) > 0:

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

    def do_flip(self, method="random_once"):
        # flips two random indices, for now
        if method == "random_once":
            two_indices = np.array([random.randint(0, self.length_state-1) for _ in range(2)])
            while two_indices[0] == two_indices[1]:
                two_indices[0] = random.randint(0, self.length_state-1)
            self.state[two_indices] = self.state[np.flip(two_indices)]
        elif method=="random_multiple":
            for x in range(5):
                self.do_flip(method="random")
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
