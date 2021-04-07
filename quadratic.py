# to run this project: main.py
# made by Thiago M Nóbrega

import matplotlib.pyplot as plt
from numpy import sqrt
import os

def Circle():
    """ This function was an attempt to solve the game using logic
    """
    amount = []
    x = -2
    while x <= 2: 
        
        y = sqrt(4-(x**2))
        print("x: ", x)
        print("y: ", y)
        plt.plot(x,y,"ro")
        # x = x + 0.001
        x = x + 0.001
        amount.append(x)

    x = -2
    while x <= 2:
        
        y = -sqrt(4-(x**2))
        print("x: ", x)
        print("y: ", y)
        plt.plot(x,y,"ro")
        # x = x + 0.001
        x = x + 0.001
        amount.append(x)

    plt.show()
    print("points: ", len(amount))
    print("lines: ", (len(amount))/2)

    print("press 1 to go back to main menu: ")
    while True:
        try:
            x = int(input('Your choice: '))
            break
        except:
            print("Invalid option. Please try again.")
        
    if x == 1:
        os.system('cls||clear')
        from main import main
        main()
    else:
        print("sorry, not an option")