import math as m
import matplotlib.pyplot as plt

#def Parametric():
i = 0.0
r = 1
x = []
y = []
lines = int(input("how many lines?"))
while i < lines+1:
    cos = m.cos(i)
    sin = m.sin(i)
    rcos = r*cos
    rsin = r*sin
    x.append(rcos)
    y.append(rsin)
    del rcos, rsin
    i = i + 1

plt.scatter(x,y)
plt.plot(x, y)
plt.show()
"""
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
"""