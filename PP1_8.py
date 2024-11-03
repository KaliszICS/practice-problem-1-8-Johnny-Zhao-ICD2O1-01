'''
    Pracitce Questions: Boolean Logic
    Author: Johnny Zhao
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
  bool1Q1 = True #assign "True" to the first boolean
  bool2Q1 = False #assign "False" to the first boolean
  print(bool1Q1 and bool2Q1) #comparing boolean 1 & 2 using and then outputting it
  print(bool1Q1 or bool2Q1) #comparing boolean 1 & 2 using or then outputting it

def q2():
  numQ2 = input("Enter an integer: ") #asking the user to input an integer
  numQ2 = int(numQ2) #turning their result into an integer datatype
  print(not(numQ2 == 0)) #testing if their input is not 0(True or False) and outputting it

def q3():
  numQ3 = input("Enter a number: ") #asking the user to input a number
  numQ3 = float(numQ3) #turning the number into a float datatype
  print(numQ3 == 0 or numQ3 > 0 and numQ3 < 11) #testing if their input is between 0 and 10(inclusive)(True or False) and outputting it

def q4():
  foodQ4 = input("Input food: ") #asking the user to input a food
  drinkQ4 = input("Input drink: ") #asking the user to input a drink
  foodQ4 = str(foodQ4) #turning their food result into a string datatype
  drinkQ4 = str(drinkQ4) #turning their drink result into a string datatype
  print(not(foodQ4 == "pizza" and drinkQ4 == "pop")) #testing if their input is not pizza and pop(True or False) and outputting it

def q5():
  numQ5 = input("Enter an integer: ") #asking the user to input an integer
  numQ5 = int(numQ5) #turning their result into an integer datatype
  boolQ5 = numQ5 % 2 == 0 #checking if their result is an even number
  print(f"The integer {numQ5} is {boolQ5}") #outputting their result in the format of: "The integer _their input_ is _True or False(wether if its a even number)_"

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''