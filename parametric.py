import math as m
import matplotlib.pyplot as plt
import os

def Circle():
    i = 0.0
    r = int(input("Size of the radius of the circle: (please use int values)"))
    x = []
    y = []
    lines = int(input("how many lines? "))
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

    while True:
        
        print("1. move to the left")
        print("2. move to the right")
        print("3. move up")
        print("4. move down")

        print("5. move diagonal up-left")
        print("6. move diagonal up-right")
        print("7. move diagonal down-left")
        print("8. move diagonal down-right")

        print("9. Main Menu")
        pick = int(input("Your pick: "))

        if pick == 1:
            #left
            x1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in x:
                x1.append(points-change)
            plt.scatter(x1,y)
            plt.plot(x1, y)
            plt.show()
            del pick, change, x1

        elif pick == 2:
            #right
            x1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in x:
                x1.append(points+change)
            plt.scatter(x1,y)
            plt.plot(x1, y)
            plt.show()
            del pick, change, x1

        elif pick == 3:
            #up
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in y:
                y1.append(points+change)
            plt.scatter(x,y1)
            plt.plot(x, y1)
            plt.show()
            del pick, change, y1

        elif pick == 4:
            #down
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in y:
                y1.append(points-change)
            plt.scatter(x,y1)
            plt.plot(x, y1)
            plt.show()
            del pick, change, y1


        elif pick == 5:
            # diagonal up-left
            x1 = []
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in x:
                x1.append(points-change)
            for points in y:
                y1.append(points+change)
            plt.scatter(x1,y1)
            plt.plot(x1, y1)
            plt.show()
            del pick, change, x1

        elif pick == 6:
            #diagonal up-right
            x1 = []
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in x:
                x1.append(points+change)
            for points in y:
                y1.append(points+change)
            plt.scatter(x1,y1)
            plt.plot(x1, y1)
            plt.show()
            del pick, change, x1

        elif pick == 7:
            #diagonal down-left
            x1 = []
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in y:
                y1.append(points-change)
            for points in x:
                x1.append(points-change)
            plt.scatter(x1,y1)
            plt.plot(x1, y1)
            plt.show()
            del pick, change, y1

        elif pick == 8:
            #diagonal down-right
            x1 = []
            y1 = []
            change = int(input("How many much would you like to move to the left? (please use integers) "))
            for points in y:
                y1.append(points-change)
            for points in x:
                x1.append(points+change)
            plt.scatter(x1,y1)
            plt.plot(x1, y1)
            plt.show()
            del pick, change, y1
        
        
        elif pick == 9:
            from main import main
            os.system('cls||clear')
            main()