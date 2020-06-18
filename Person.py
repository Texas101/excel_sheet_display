import random
from enum import Enum
from Virus import *

class State(Enum):
    HEALTHY = 1
    # LATENT = 2
    INFECTED = 3

class PerceivedState(Enum):
    UNKNOWN = 0
    SUSPECTED = -1
    CURED = 1
    HEALTHY = 2
    INFECTED = -2

class Person:

    def __init__(self, pos):
        self.pos = pos
        self.state = State.HEALTHY
        self.perceived_state = PerceivedState.UNKNOWN
        # self.is_unknown = True
        # self.flagged = False
        self.infection_time = 0
        self.virus = None
        self.bad_cure_infection_rate = 0.25  # TODO: make this RNG

    def test_infected(self):
        if self.state == State.INFECTED:
            self.perceived_state = PerceivedState.INFECTED
            return True
        else:
            if self.perceived_state == PerceivedState.UNKNOWN:
                self.perceived_state = PerceivedState.HEALTHY
            return False

    def cure_patient(self, virus):
        if self.state != State.HEALTHY:
            self.state = State.HEALTHY
            self.perceived_state = PerceivedState.CURED
            # TODO: implement scoring
            self.infection_time = 0
            self.virus = None
        else:
            if random.random() < self.bad_cure_infection_rate:
                # TODO: update score
                self.perceived_state = PerceivedState.INFECTED
                self.get_infected(virus)

    def update(self):
        if self.state > State.HEALTHY:
            self.infection_time += 1

    def get_infected(self, virus):
        self.state = State.INFECTED
        self.virus = virus
        # self.infection_time += 1

    def flag(self):
        self.perceived_state = PerceivedState.SUSPECTED

    def __str__(self):
        if self.perceived_state == PerceivedState.SUSPECTED:
            return '?'
        elif self.perceived_state == PerceivedState.CURED:
            return 'c'
        elif self.perceived_state == PerceivedState.HEALTHY:
            return 'h'
        elif self.perceived_state == PerceivedState.INFECTED:
            return 'x'
        else: ## Unknown
            return 'o'

    def __repr__(self):
        return self.__str__()