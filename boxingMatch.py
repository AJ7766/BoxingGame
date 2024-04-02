from boxer import Boxer
from person import Person
import time

class BoxingMatch():
    def __init__(self, boxer1, boxer2, date, city):
        self.boxer1 = boxer1
        self.boxer2 = boxer2
        self.date = date
        self.city = city
    
    """a method to start a match between two boxers"""
    def start_match():
        #creating two variables to check if the boxers were found
        boxer1_found = False
        boxer2_found = False

        while not boxer1_found: #a loop that will run until boxer1 is found
            user_input = input("Please enter a Boxer's Number you wish to participate: ")   #user inputs a boxers number
            for boxer in Boxer.boxers_list: #looping through all our boxers
                boxer.boxing_number = Boxer.boxers_list.index(boxer)    #we assign a boxing number to every boxer
                if str(boxer.boxing_number) == user_input:  #if the input matches the boxers number
                    print(f"The first Boxer is {boxer.name}!")  #prints out the boxers name we wanted
                    boxer1_found = True #sets the boxer1 found to true
                    boxer1 = boxer  #sets boxer1 = boxer
            if not boxer1_found:    #if the boxer is not found the user has to keep giving an input because boxer1 found is False
                print(Person.text_break)
                print("Boxer not found")
                print(Person.text_break)

        """identical as above but just for boxer2"""
        while not boxer2_found:
            user_input = input("Please enter a Boxer's Number you wish to participate: ")
            for boxer in Boxer.boxers_list:
                boxer.boxing_number = Boxer.boxers_list.index(boxer)
                if str(boxer.boxing_number) == user_input:
                    print(f"The second Boxer is {boxer.name}!")
                    boxer2_found = True
                    boxer2 = boxer
            if not boxer2_found:
                print(Person.text_break)
                print("Boxer not found")
                print(Person.text_break)
        print(Person.text_break)
        """after we found our 2 boxers"""
        boxingMatch = BoxingMatch(boxer1, boxer2, "12/12-2014", "Malmö, Sweden")#we create an object(Boxing Match in this case) through our BoxingMatch class
        print(f"{boxingMatch.boxer1.name} will be fightning {boxingMatch.boxer2.name} in {boxingMatch.city}, {boxingMatch.date}.")  #a print of which fighters are figthing and where and when
        print("Calculating which boxer have a better chance of winning...")
        time.sleep(0.5) #a 0.5sec delay of reading the below

        """i wanted to compare the two boxers and see who has a higher chance of winning, so basicly what i thought was to compare their age, height and weight, so whenever the boxer has an advantage over the other boxer in one of the categories the boxer will gain +1 point and if it's identical no points will be given to either"""
        boxer1_points = 0
        boxer2_points = 0
        while True: #a loop that will go on until a break
            if int(boxingMatch.boxer1.age) < int(boxingMatch.boxer2.age):
                boxer1_points += 1
            elif int(boxingMatch.boxer2.age) < int(boxingMatch.boxer1.age):
                boxer2_points += 1
            elif int(boxingMatch.boxer1.age) == int(boxingMatch.boxer2.age):
                pass
            elif int(boxingMatch.boxer1.height) < int(boxingMatch.boxer2.height):
                boxer2_points += 1
            elif int(boxingMatch.boxer2.height) < int(boxingMatch.boxer1.height):
                boxer1_points += 1
            elif int(boxingMatch.boxer2.height) == int(boxingMatch.boxer1.height):
                pass
            elif int(boxingMatch.boxer1.weight) < int(boxingMatch.boxer2.weight):
                boxer2_points += 1
            elif int(boxingMatch.boxer2.weight) < int(boxingMatch.boxer1.weight):
                boxer1_points += 1
            elif int(boxingMatch.boxer2.weight) == int(boxingMatch.boxer1.weight):
                pass
            if (boxer2_points < boxer1_points): #if boxer1 has more points than boxer2, boxer1 has a higher chance of winning
                print(Person.text_break)
                print(f"After calculating the boxers age, height and weight there is a higher chance that {boxer1.name} will come out victorious!")
                print(Person.text_break)
                break
            elif (boxer1_points < boxer2_points):
                print(Person.text_break)
                print(f"After calculating the boxers age, height and weight there is a higher chance that {boxer2.name} will come out victorious!")
                print(Person.text_break)
                break
            elif (boxer1_points == boxer2_points):  #if the points end up the same it's gonna print out that it's most likely gonna end up in a draw
                print(Person.text_break)
                print(f"After calculating the boxers age, height and weight they are very equal in terms of stats, it might end in a draw!")
                print(Person.text_break)
                break
