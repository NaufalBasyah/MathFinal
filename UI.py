'''
Methods to interact with program and calculate by given user input

@author : Imanuel Febie, 2201835800
'''
from MathMethods import *

run_progam = True

def home_view():
    '''
    Show the options and choose by int input
    '''

    print("Choose one of following options:")
    print()
    print("[1] Root Newton")
    print("[2] Bisection Root")
    print("[0] Exit")

    print("")

    choice = int(input("Choice: "))

    # Call function based on user input
    if choice == 1:
        root_newton_view()
    elif (choice == 0):
        exit() # Stops the program
        

def root_newton_view():
    '''
    Ask user to input f and xpoint
    '''

    print('Root finding using Newton method (input f and xpoint)')
    print("")
    f = input("F = ") # input f
    xpoint = int(input("X point = ")) # input x

    rootNewton(f, xpoint)
    
while run_progam:
        home_view() # call function to run the program


