# to run this project: main.py
import os

def main():
    print("press 1 to make graph a circle using a quadritic function")
    print("press 2 to make graph a circle using a prametric function")
    print("press 3 to exit \n")
    while True:
        try:
            x = int(input('Your choice: '))
            break
        except:
            print("Invalid option. Please try again.")
        
    if x == 1:
        del x
        os.system('cls||clear')
        from quadratic_function import QuadraticFunction
        QuadraticFunction()
    if x ==2:
        del x
        os.system('cls||clear')
        from parametric import Circle
        Circle()
    if x == 3:
        del x
        os.system('cls||clear')
        print("\nthank you so much for you time!\n")
        exit()
    else:
        print("sorry, not an option")
main()