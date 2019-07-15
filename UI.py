'''
@author : Imanuel Febie, 2201835800

PROJECT GROUP:
- Imanuel Febie
- Naufal Basyah

PROJECT DESCRIPTION
-------------------
With the time we had we decided to do a text based program that solves the following problems:
1. Root finding
    - Newton Method
    - Bisection Method
2. Central differentiation
'''
from MathMethods import *
import sys

run_progam = True

def home_view():
    '''
    Show the options and choose by int input
    '''

    print("Choose one of following options:")
    print()
    print("[1] Root Newton")
    print("[2] Bisection Root")
    print("[3] Central Difference")
    print("[0] Exit")

    print("")

    choice = int(input("Choice: "))

    # Call function based on user input
    if choice == 1:
        root_newton_view()
        
    elif choice == 2:
        bisectionView()
    
    elif choice == 3:
        central_view()
        
            
    elif (choice == 0):

        sys.exit() # Stops the program
        

def root_newton_view():
    '''
    Ask user to input f and xpoint
    '''

    print('Root finding using Newton method (input f and xpoint)')
    print("")
    f = input("F = ") # takes equation in string form
    xpoint = int(input("X point = ")) # input x

    rootNewton(f, xpoint)
   
def bisectionView():
    '''
    Root finding using bisection method
    '''

    print("Root finding using bisection method")
    print()
    
    f = input("F = ") # takes equation in string form
    xu = int(input("Upper Bound: "))
    xl = int(input("Lower Bound:"))
    
    print(bisectionRoot(f,xl,xu))
    
def central_view():
    '''
    Calculates the central difference with input from the user
    '''

    print("Calculte the central difference")
    print()
    f = input("F = ")
    xpoint = int(input("X Point: ")) # takes equation in string form
    xu = int(input("Upper Bound: "))
    xl = int(input("Lower Bound:"))

    centralDiffApp(f,xpoint,xl,xu)
   

while run_progam:
        # run the program
        home_view() # call function to run the program


