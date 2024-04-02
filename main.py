from person import Person
from boxer import Boxer
from menu import * #everything from menu.py
from coach import Coach
from organisation import Organisation

#creating three organisations through Organisation class
WBO = Organisation("World Boxing Organization", "USA")
WBC = Organisation("World Boxing Council", "Mexico")
WBA = Organisation("World Boxing Association", "USA")

#creating three coaches objects through coach class
coachManny = Coach("Manny Pacquiao", "Male", 30, WBO.name)
coachFloyd = Coach("Floyd Mayweather", "Male", 26, WBA.name)
coachShakur = Coach("Shakur Stevenson", "Male", 26, WBC.name)

#creating 4 boxers and then applying them into boxer_list
tyson = Boxer("Tyson", "Male", 30, "1.78", "100", "London, United Kingdom", coachManny.name, WBO.name)
Boxer.boxers_list.append(tyson)
WBO.boxers.append(tyson)

josh = Boxer("Josh", "Male", 35, "1.73", "70", "Madrid, Spain", coachShakur.name, WBC.name)
Boxer.boxers_list.append(josh)
WBC.boxers.append(josh)

josefine = Boxer("Josefine", "Female", 23, "1.60", "60", "Jönköping, Sweden", coachManny.name, WBO.name,["Lightweight Champion", "Heavyweight Champion"])
Boxer.boxers_list.append(josefine)

emma = Boxer("Emma", "Female", 25, "1.70", "70", "Köpenehamn, Denmark", coachFloyd.name, WBA.name,["Lightweight Champion"])
Boxer.boxers_list.append(emma)

print(Person.text_break)
print("Jackies Boxers List")
print(Person.text_break)
get_menu() #calling the menu
