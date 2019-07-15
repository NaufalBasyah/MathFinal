'''
Methods to interact with program and calculate by given user input

@author : Imanuel Febie, 2201835800
'''
from MathMethods import *
import sys

run_progam = True
1
def home_view():
    '''
    Show the options and choose by int input
    '''

    print("Choose one of following options:")
    print()
    print("[1] Root Newton")
    print("[2] Bisection Root")
#    print("[3] Central Difference")
    print("[0] Exit")

    print("")

    choice = int(input("Choice: "))

    # Call function based on user input
    if choice == 1:
        root_newton_view()
        
    elif choice == 2:
        bisectionView()
    
    # elif choice == 3:
    #     centralView()
        
            
    elif (choice == 0):
        
        
        sys.exit() # Stops the program
        

def root_newton_view():
    '''
    Ask user to input f and xpoint
    '''

    print('Root finding using Newton method (input f and xpoint)')
    print("")
    f = input("F = ") # input f
    xpoint = int(input("X point = ")) # input x

    rootNewton(f, xpoint)
   
def bisectionView():
    print("Root finding using bisection method")
    print()
    
    f = input("F = ")
    xu = int(input("Upper Bound: "))
    xl = int(input("Lower Bound:"))
    
    print(bisectionRoot(f,xl,xu))
    
#def centralView():
#    
#    f = input("F = ")
#    xpoint = int(input("X Point: "))
#    xu = int(input("Upper Bound: "))
#    xl = int(input("Lower Bound:"))
#    
#    centralDiffApp(f,xpoint,xl,xu)
#    

    
    

    
while run_progam:
        home_view() # call function to run the program


