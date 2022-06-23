import random as random
import algo1 as algo1

dir = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

def filltxt(name, n):
    with open("data/ships.txt", "+a") as file:
        for i in range(n):
            file.write(name
        +str(i)
        +" "
        +str(random.randint(-n+1, n-1)+random.random())
        +" "
        +str(random.randint(-n+1, n-1)+random.random())
        +" "
        +dir[random.randint(0,7)]
        +"\n")