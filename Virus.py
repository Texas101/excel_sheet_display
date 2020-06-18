import random

class Virus:

    def __init__(self, name, infection_rate=0.7, reinfection_rate=0.05):
        self.name = name
        self.infection_rate = infection_rate
        self.reinfection_rate = reinfection_rate
        self.transmit_range = 1

    def spread(self, reinfection):
        if reinfection:
            if random.random() < self.reinfection_rate:
                return True
        else:
            if random.random() < self.infection_rate:
                return True

        return False

