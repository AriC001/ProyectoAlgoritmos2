import random as random
import algo1 as algo1

dir = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

def filltxt(name, n):
    with open("data/ships.txt", "w") as file:
        for i in range(n):
            file.write(name
        +str(i)
        +" "
        +str(random.randint(-n, n))
        +" "
        +str(random.randint(-n, n))
        +" "
        +dir[random.randint(0,7)]
        +"\n")