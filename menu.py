from person import Person
from boxer import Boxer
from boxingMatch import BoxingMatch

"""It's a method to basicly print out the menu for the user to choose from"""
def get_menu():
    user_input1 = ""    #creating an empty string
    user_input2 = ""
    
    while user_input1 != "0":   #loop at keeps printing out the Menu unless the input is "0"
        print("1) Boxing Match!")
        print("2) Show Boxers")
        print("3) Edit/Remove Boxers")
        print("4) Add Boxer")
        print("0) Exit")
        user_input1 = input("Make a choice: ")  #user makes their choice
        if(user_input1 == "1"): #if input is "1" it runs 2 methods, first one which is a method from Boxer class that prints out all the boxers, second method is starting a boxing match which is imported from boxingmatch.py
            print(Person.text_break)
            print("Here is a list of all Boxers!")
            Boxer.print_all_boxers()
            BoxingMatch.start_match()
        if user_input1 == "2":  #if the user input is "2" another loop withh be going on, pretty much the same as the one above but with a different menu this time
            user_input2 = "" 
            while user_input2 not in ["0", "1", "2", "3"]:
                print("1) Show all Boxers")
                print("2) Show only Female boxers")
                print("3) Show only Male boxers")
                print("0) Exit")
                user_input2 = input("Make a choice: ")  # Use user_input2 here
                if user_input2 == "1":  #in the nested-loop if the user inputs "1", it shows all the boxers through the method
                    print(Person.text_break)
                    print("Here is a list of all Boxers!")
                    Boxer.print_all_boxers()
                elif user_input2 == "2":    #"2" its gonna show all female boxers through the method
                    print(Person.text_break)
                    print("Here is a list of all Female Boxers!")
                    Boxer.print_female_boxers()
                elif user_input2 == "3":
                    print(Person.text_break)
                    print("Here is a list of all Male Boxers!")
                    Boxer.print_male_boxers()
                elif user_input2 == "0":
                    print(Person.text_break)
                    print("Bye!")
                    print(Person.text_break)
                    break   #exit the sub-menu loop
        elif(user_input1 == "3"):   #"3" it first prints out all boxers and then a method that lets the user input the boxers number to edit/remove
            Boxer.print_all_boxers()
            print("Enter a Boxers Number you want to remove/edit!")
            Boxer.get_boxer()
        elif(user_input1 == "4"):   #"4" method to add a new boxer through a method
            print(Person.text_break)
            print("Add a new Boxer(Name, Age, Gender, Height, Weight, Belt)")
            Boxer.add_boxer()
        elif(user_input1 == "0"):   #"0" breaks the main loop and exits
            print(Person.text_break)
            print("Bye!")
            break
        if user_input1 not in ["0", "1", "2", "3", "4"]:    #anything that is inputed that is not 0-4 will be a invalid choice
            print(Person.text_break)
            print("Invalid choice. Please choose a valid option.")