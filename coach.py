from person import(Person)

class Coach(Person):
    def __init__(self, name, gender, age, organisation):
        super().__init__(name, gender, age)
        self.organisation = organisation