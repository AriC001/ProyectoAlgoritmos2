from main import *
from random import *
from myarray import *
import linkedlist

dir = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

def filltxt(name, n):
    with open("data/ships.txt", "w") as file:
        file.write("01/05/2022"+"\n")
        for i in range(n):
            file.write(name
        +str(i)
        +" "
        +str(randint(-n+1, n-1)+random.random())
        +" "
        +str(randint(-n+1, n-1)+random.random())
        +" "
        +dir[randint(0,7)]
        +"\n")

def create_fleet():
    result = []
    directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']

    # Random points.
    for i in range(20):
        point_r1 = (randrange(100), randrange(100), directions[randrange(len(directions) - 1)])
        point_r2 = (randrange(100), randrange(100), directions[randrange(len(directions) - 1)])
        result.append(point_r1)
        result.append(point_r2)
    #Lateral point. Estos barcos van a tener riesgo de colision el dia 10 y el 11.
    for i in range(20):
        point_left = (-10, i, 'E')
        point_right = (10, i, 'W')
        result.append(point_left)
        result.append(point_right)
    #Vertical point. Estos barcos van a tener riesgo de colision el dia 5.
    for i in range(20):
        point_down = (i+12, -5, 'N')
        point_up = (i+12, 4, 'S')
        result.append(point_down)
        result.append(point_up)
    #Diagonal point. Estos barcos van a tener riesgo de colision los primeros 20 dias pues van por la misma diagonal.
    for i in range(20):
        point_up = (i, i, 'SW')
        point_down = (-i, -i, 'NE')
        result.append(point_up)
        result.append(point_down)
    # Random points
    for i in range(20):
        point_r1 = (randrange(100), randrange(100), directions[randrange(len(directions) - 1)])
        point_r2 = (randrange(100), randrange(100), directions[randrange(len(directions) - 1)])
        result.append(point_r1)
        result.append(point_r2)
    return result

'''create from txt'''
create()

'''-search <date> <nombre_embarcacion>'''
# print(search("01/05/2022", "b1"))
# print(search("01/05/2022", "b2"))


'''navigation_system.py -closer <date>'''
# C = closer("01-05-2022")
# print(C)


'''navigation_system.py -closer <date>'''
print(linkedlist.length(collision()))