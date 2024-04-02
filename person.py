class Person:
    
    text_break = ("-" * 20) #it's a universal text divider that I've been using in most modules

    def __init__(self, name, gender, age):  #initializing attributes for Person
        self.name = name
        self.age = age
        self.gender = gender