'''
Methods to interact with program and calculate by given user input
'''
from MathMethods import *


def home_view():
    '''
    Show the options and choose by int input
    '''

    print("Choose one of following options:")
    print()
    print("[1] Differiante")
    print("[2] Root Newton")
    print("[3] Bisection Root")
    print("[4] Central Differentiation")

    print("")

    choice = int(input("Choice: "))

    # Call function based on user input
    if choice == 2:
        root_newton_view()
        

def differantiate_view():
    pass

def root_newton_view():
    '''
    Ask user to input f and xpoint
    '''

    print('Root finding using Newton method (input f and xpoint)')
    print("")
    f = input("F = ")
    xpoint = int(input("X point = "))

    rootNewton(f, xpoint)

def bisection_root_view():
    '''
    Ask user for f1, a and b
    '''
    
    print("This functions takes (f1, a, b)")
    print()
    

home_view()


