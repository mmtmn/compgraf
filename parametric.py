import math as m
import matplotlib.pyplot as plt

def Parametric():
    x = 0.0
    r = 1
    while x < 10:
        cos = m.cos(x)
        sen = m.sin(x)
        plt.plot(r*cos,r*sen,"ro")
        x = x + 0.01
    plt.show()

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