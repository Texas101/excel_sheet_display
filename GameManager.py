
from Person import *
from Virus import *
import random, time

class GameManager:

    def __init__(self):
        random.seed(time.time())
        self.virus = Virus('AHRHLJKSDFLKH', infection_rate=0.3, reinfection_rate=0.05)
        self.people_count = 20
        self.person_list = []
        self.start_infected = 2
        self.initialize()

    def initialize(self):

        for i in range(1,self.people_count+1):
            self.person_list.append(Person(i))

        local_counter = 0
        while local_counter < self.start_infected:
            potential_candidate = random.choice(self.person_list)
            if potential_candidate.state == State.HEALTHY:
                potential_candidate.get_infected(self.virus)
                local_counter += 1

            # self.person_list[infected_person].get_infected(self.virus)
        self.initialize_display()

    def initialize_display(self):
        print(f"Hello Doctor, and welcome to our Virus Game. Your objective is to cure the infected and save the day!"
              f"The rules are simple. Displayed before you will be a list of {self.people_count} o's. Each of o represents a person in a list. Above each o, there will be a number indicating their position on the list."
              f"As the Doctor, each turn you'll have to either test or cure a single person in the list. But beware! Every turn, there will be a chance for the virus to spread from the infected people to their immediate neighbors and curing a healthy person may actually give them the virus instead."
              f"To make things easier, you can flag individuals you suspect of having the virus for your future turns."
              f"So, do you have what it takes?  "
              f""
              f"CONTROLS:"
              f"")



    def gameloop(self):
        # TODO: main loop that runs the game. User input, then rendering
        #Step 1, make the while loop that does the three actions
        #Step 2, alter the display as a result of said actions.
        # self.initialize()
        # self.is_game_over = False
        while not self.is_game_over():
            # self.is_game_over = self.is_game_over()
            try:
                self.display()
                inputs = input("> ").upper().split(' ')
                # in1 = input("Would you like to: Flag, Test, or Cure? ").upper()
                if inputs[0] == 'FLAG':
                #TODO: maybe maker this a indented loop so people can type other stuff?
                    #Flag self
                    # in2 = int(input('What number would you like to Flag? '))
                    self.run_flag(int(inputs[1]))
                    # self.run_flag(self.{in2})

                    #TODO: What would happen if they tried to flag multiple people and it all went to the variable in2?
                if inputs[0] == 'TEST':
                    # in3 = int(input('What number would you like to Test?'))
                    self.run_test(int(inputs[1])) #TODO: person_list in place for like person in the list. idk how to say dat
                    self.spread_infection()

                if inputs[0] == 'CURE':
                    # in4 = int(input('What number would you like to Cure?'))
                    self.run_cure(int(inputs[1]))
                    self.spread_infection()
                else:
                    print(f"Try Spelling {inputs[0]} Better. ")
                    #TODO: Make sure this goes back to the beginning of gameloop
            except ValueError as e:
                print(f"Entered Input is invalid! {inputs} does not contain a number. try again")

        print("Congratulations! Game over!")



    def spread_infection(self):
        # Run at the end of the gameloop
        # For each person in self.person_list, if they're infected, run the virus.spread()
        # make a new list of people as you go
        for person in self.person_list:
            if person.state == State.INFECTED:
                for i in range(person.pos - self.virus.transmit_range, person.pos + self.virus.transmit_range):

                    if i == person.pos or self.person_list[i-1].state == State.INFECTED:
                        continue
                    if self.person_list[i-1].perceived_state == PerceivedState.CURED:
                        should_spread = person.virus.spread(True)
                    else:
                        should_spread = person.virus.spread(False)
                    if should_spread:
                        self.person_list[i-1].get_infected(self.virus)
                    # spread to both sides

        # TODO: call update function for each person before spreading the virus
        pass

    def display(self):
        pos = ""
        people = ""
        for person in self.person_list:
            if person.pos < 10:
                pos += f'{person.pos}  '
                people += f'{person}  '
            else:
                pos += f'{person.pos} '
                people += f'{person}  '

        print(pos)
        print(people)


    def run_test(self, position):
        # Runs the test method on the person at position in self.people_list
        self.person_list[position-1].test_infected()



    def run_cure(self, position):
        # Attempts to Cure
        self.person_list[position - 1].cure_patient(self.virus)
        # Need to pass self.virus when attempting to cure, just in case the person is actually healthy

    def run_flag(self, position):
        # Flag a person as "Suspected"

        self.person_list[position-1].flag()
        #in2 = whatever number they keep in
    def update_score(self):
        # TODO: implement
        # Depends on gameplay
        pass

    def is_game_over(self):
        """
        if
        Something to tie in Percieved State Healthy/Infected to PersoneCount or Person List. Maybe using a counter and equalling it to people_count?
        Stop main game loop(using a should_continue_function?)


        """
        # Check for all infected:
        are_all_ill = True
        for person in self.person_list:
            if person.state != State.INFECTED:
                are_all_ill = False
        if are_all_ill:
            return True
        else:
            # Check for Healthy
            for person in self.person_list:
                if person.state == State.INFECTED:
                    return False
            return True
if __name__ == '__main__':
    GM = GameManager()
    GM.gameloop()
        # Return true if all people are healthy
        # Return true if everyone is infected (haha #wrekt)


