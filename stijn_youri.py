
import random
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

            print(f"\rtime {timestep}, score {score}, patience {self.patience}", end='')

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


