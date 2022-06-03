from algo1 import* 
from linkedlist import*
import objects as obj
import dictionary as dict
import algo1 as algo1

def create():

    file = open("data/ships.txt", "r")
    lines = file.readlines()
    lslen = len(lines)
    dictionary = dict.Dictionary(lslen-1)

    for i in range(1, lslen):

        attrno = 0
        llen = len(lines[i])
        for j in range(llen):

            if lines[i][j] == " " and attrno == 0:
                id = algo1.substr(lines[i], 0, j)
                start = j+1
                attrno += 1

            elif lines[i][j] == " " and attrno == 1:
                x = algo1.substr(lines[i], start, j)
                start = j+1
                attrno += 1

            elif lines[i][j] == " " and attrno == 2:
                y = algo1.substr(lines[i], start, j)
                start = j+1
                attrno += 1

            elif j == llen-1:
                direction = algo1.substr(lines[i], start, j)

        dictionary.insert(obj.Ship(id, x, y, direction))

    file.close()
    
    return dictionary