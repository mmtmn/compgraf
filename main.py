# to run this project: main.py
# made by Thiago M Nóbrega

import os

def main():
    print("Press 1 to graph circle using a parametric equation")
    print("Press 2 to graph a elipse using a parametric equation")
    print("Press 3 to graph a circle using a quadritic function")
    print("Press 4 to exit \n")
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
        print("\nThank you so much for you time!\n")
        exit()
    else:
        print("Sorry, that's not an option")

main()