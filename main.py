# to run this project: main.py
# made by Thiago M Nóbrega

import os

def main():
    print("press 1 to graph circle using a parametric equation")
    print("press 2 to graph a elipse using a parametric equation")
    print("press 3 to graph a circle using a quadritic function")
    
    print("press 4 to exit \n")
    while True:
        try:
            x = int(input('Your choice: '))
            break
        except:
            print("Invalid option. Please try again.")  
    if x == 1:
        del x
        os.system('cls||clear')
        from parametric import Circle
        Circle()
    elif x == 2:
        del x
        os.system('cls||clear')
        from parametric import Ellipse
        Ellipse()
    elif x ==3:
        del x
        os.system('cls||clear')
        from quadratic import Circle
        Circle()
    elif x == 4:
        del x
        os.system('cls||clear')
        print("\nthank you so much for you time!\n")
        exit()
    else:
        print("sorry, that's not an option")

main()