from person import Person

class Boxer(Person):
    #creating three private lists
    boxers_list = []
    female_boxers = []
    male_boxers = []
    
    """we have some attributes here and city,coach,organisation,belts have a default value"""
    def __init__(self, name, gender, age, height, weight, city="Malmö, Sweden", coach="Zlatan", organisation="MAU", belts=None):
        super().__init__(name, gender, age) #accessing the 3 attributes of it's parent class(Person)
        self.height = height
        self.weight = weight
        self.city = city
        self.coach = coach
        self.organisation = organisation
        self.belts = belts if belts is not None else [] #if there is are no belts appended, belts=None
    """a function to print a boxers info, (self) refers to the classes instances, in this case its a boxer being passed in as a parameter, for example if we pass in boxer "Tyson" we will get all of Tysons information"""
    def print_boxer_info(self):
        print(f"- Name: {self.name} | Gender: {self.gender} | Age: {self.age} | City: {self.city}")
        print(f"- Height: {self.height} m | Weight: {self.weight} kg")
        print(f"- Organisation: {self.organisation} | Coach: {self.coach}")
        if self.belts:  #if there are belts, then it's going to print out every belt, else no belts
            print("Belts:")
            for belt in self.belts:
                print(f"- {belt}")
        else:
            print("- No belts yet")

    """method to print all female boxers"""
    @classmethod    #@classmethod means its first parameter is going to recieve the class itself and in this case Boxer(cls)
    def print_female_boxers(cls):   #cls is basicly a short term of "class"
        
        for boxer in cls.boxers_list:   #we are making a for-loop for every boxer in boxers_list
            if(boxer.gender.lower() == "female"):   #if boxers gender is "female", the female boxer is appended to the female_boxers list
                cls.female_boxers.append(boxer)
            else:
                pass
        """after we got our female boxers in the female_boxers list we have to print them out, as seen below"""
        female_boxers_length = len(cls.female_boxers)   #we are creating a variable to track the length of our female_boxers list
        for i, female in enumerate(cls.female_boxers):  #a for-loop where we can assign index as "i" and also can loop through every female boxer in our list
            print(Person.text_break)
            print(f"Boxer Number: {i}") #{i} stands for index
            female.print_boxer_info()   #we are printing out the female boxer in our list through print_boxer method
            if(i == female_boxers_length - 1): #here we have an if-statement on the last boxer in the list, we then print a text-break
                print(Person.text_break)
            else:
                pass

    """this method is identical to the female one but its just the male version"""
    @classmethod
    def print_male_boxers(cls):
        for boxer in cls.boxers_list:
            if(boxer.gender.lower() == "male"):
                cls.male_boxers.append(boxer)
            else:
                pass
        male_boxers_length = len(cls.male_boxers)
        for i , male in enumerate(cls.male_boxers):
            print(Person.text_break)
            print(f"Boxer Number: {i}")
            male.print_boxer_info()
            if(i == male_boxers_length - 1):
                print(Person.text_break)
            else:
                pass

    """identical method to female and male boxer function, but instead we use the boxers_list(which contains every boxer regardless of gender)"""
    @classmethod
    def print_all_boxers(cls):
        total_boxers = len(cls.boxers_list) 
        for i, boxer in enumerate(cls.boxers_list):
            print(Person.text_break)
            print(f"Boxer Number: {i}")
            boxer.print_boxer_info()
            if(i == total_boxers - 1):
                print(Person.text_break)
            else:
                pass
    """a function to get a specific boxer, but also in this function we are able to edit/remove a specific boxer depending on their boxing number"""
    @classmethod
    def get_boxer(cls):
        user_input = ""
        user_input_2 = ""
        boxer_found = False #a variable to check if a boxer is found, set to false as default

        while not boxer_found:  #this loop while keep on going until a boxer is found
            user_input = input("Enter a Boxer's Number: ")  #user inputs a boxer's number
            for boxer in cls.boxers_list:   #looping thorugh every boxer in our boxer list
                boxer.boxing_number = cls.boxers_list.index(boxer)  #creating a variable for every boxer with their index as their boxer number
                if str(boxer.boxing_number) == user_input:  #if the userinput is the same as the boxers number 
                    print(Person.text_break)
                    print(f"Boxer Number {user_input}") #prints out the boxer the user selected
                    boxer.print_boxer_info()    #prints out the boxers info through the method
                    print(Person.text_break)
                    boxer_found = True  #since we found a boxer, we also set the boolean to true, to stop the loop

                    #in above we found a boxer and now we can either remove/edit the boxer depending on user input
                    while user_input_2 not in ["1", "2", "0"]:  #while the userinput is not 1,2,0 this loop will keep going
                        print("1) Edit Boxers(Name, Age, Gender, Height, Weight, Belts)")
                        print(f"2) Remove Boxer: {boxer.name}")
                        print("0) Exit")
                        user_input_2 = input("Make a choice: ") #user has a choice to make, remove/edit or exit
                        if user_input_2 == "1": #user choose to edit, the edit function will run
                            cls.edit_boxer(boxer)   #a boxer is passed in to the function
                            break   #breaks out from the loop after editing the boxer
                        elif user_input_2 == "2":
                            cls.remove_boxer(boxer) #runs remove_boxer function if 2 is input
                            break
                        elif user_input_2 == "0":   #0 to exit
                            print(Person.text_break)
                            print("Bye!")
                            print(Person.text_break)
                            break
            if not boxer_found:  #if the boxer wasnt found then this text will print out 
                print(Person.text_break)
                print("Boxer not found")
                print(Person.text_break)

    """a method to edit a boxer"""
    @classmethod
    def edit_boxer(cls, boxer):# a boxer is passed in as a parameter
        user_input = False
        new_name = ""
        new_age = ""
        new_height = ""
        new_weight = ""
        new_gender = ""

        print(Person.text_break)
        print("Editing boxer...")
        print(Person.text_break)
        while not new_name.isalpha():   #if the input is not only alphabetical its gonna keep running
            new_name = input("Enter new name(in letters): ")
        boxer.name = new_name   #if the name is alphabetical it's gonna be applied as the new name for the boxer
        while not new_age.isdigit():    #if the input is not only digits its gonna keep running
            new_age = input("Enter new age(a number): ")
        boxer.age = new_age
        while new_gender not in ["female", "male"]: #if the input is not either male or female its gonna keep running
            new_gender = input("Enter new gender(Male or Female): ").lower()    #.lower means whatever FemALE or MalE whatever the user puts in its gonna be full lower cases, this makes it easier to work with later on
        boxer.gender = new_gender
        while not new_height.isdigit():
            new_height = input("Enter new height(in centimeters): ")
        boxer.height = new_height
        while not new_weight.isdigit():
            new_weight = input("Enter new weight(in kilograms): ")
        boxer.weight = new_weight
        print(Person.text_break)
        while user_input not in ["1", "2"]:
            print("1) Add belt to the boxer")
            print("2) Remove belts from the boxer")
            user_input = input("Make a choice: ")
            if(user_input == "1"):
                new_belt = input("Enter the champions new belt: ")
                boxer.belts.append(new_belt)    #appends a new belt to the boxer
            elif(user_input == "2"):    #if it wants to remove the belts it passes a empty list
                boxer.belts = []
        print(Person.text_break)
        print("Your new Boxer is:")
        cls.print_boxer_info(boxer) #then we are printing our new boxer with our printboxer method
        print(Person.text_break)

    """a method where a boxer is passed in as a parameter to be removed"""
    @classmethod
    def remove_boxer(cls, boxer_remove):
        for boxer in cls.boxers_list:   #looping through every boxer in the boxer list
            if(boxer == boxer_remove):  #if the boxer matches the boxer we passed in as a parameter it's going to get removed from the boxer list
                cls.boxers_list.remove(boxer_remove)
                print(Person.text_break)
                print(f"Boxer {boxer.name} was removed succesfully!")
                print(Person.text_break)

    """method to add boxer"""
    @classmethod
    def add_boxer(cls):
        user_input = False
        new_boxer = ""
        name = ""
        age = ""
        height = ""
        weight = ""
        gender = ""
        belt = []

        #the default values of city, coach ,org
        city = "Sweden"
        coach = "Zlatan"
        organisation = "MAU"


        print(Person.text_break)
        while not name.isalpha():
            name = input("Enter new name(in letters): ")
        while not age.isdigit():
            age = input("Enter new age(a number): ")
        while gender not in ["female", "male"]:
            gender = input("Enter new gender(Male or Female): ").lower()
        while not height.isdigit():
            height = input("Enter new height(in centimeters): ")
        while not weight.isdigit():
            weight = input("Enter new weight(in kilograms): ")
        print(Person.text_break)
        while user_input not in ["1", "2"]:
            print("1) Add belt to the boxer")
            print("2) Skip")
            user_input = input("Make a choice: ")
            if(user_input == "1"):
                beltinput = input("Enter the champions new belt: ")
                belt.append(beltinput)
            elif(user_input == "2"):
                pass
        #after gathering all the information on our new boxer, we are creating and appending the boxer as a new object(boxer in this case) in our Boxer class
        new_boxer = Boxer(name.capitalize(), gender.capitalize(), age, height, weight, city, coach, organisation, belt) #creating the boxer
        cls.boxers_list.append(new_boxer)   #appending the boxer to the list
        print(Person.text_break)
        print("Your new Boxer is:")
        cls.print_boxer_info(new_boxer)
        print(Person.text_break)