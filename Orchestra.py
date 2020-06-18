import pprint

class Orchestra:

    def __init__(self):
        self.conductor = "Conductor"
        self.location = "Dallas"
        self.sections = []
        # self.instruments = ['violin', 'viola', 'base drum', 'bongo']
        self.budget = 100000
        self.add_section(Section('violin', 16))
        self.add_section(Section('viola', 16))
        self.add_section(Section('cello', 16))
        self.add_section(Section('base', 8))


    def add_section(self, section):
        if isinstance(section, Section):
            self.sections.append(section)
        else:
            raise TypeError("Error - this is not a Section! ")

    def change_budget(self, new_budget):
        self.budget = new_budget

    def view_sections(self):
        pprint.pprint(self.sections)

    # def add_instrument(self, new_instrument):
    #     self.instruments.append(new_instrument)



class Section:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name}: {self.size}"

    def __repr__(self):
        return f"{self.name}: {self.size}"