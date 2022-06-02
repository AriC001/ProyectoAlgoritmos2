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

# f = open("data/ships.txt","+r")
# linea1 = f.readline()
# print(linea1)
# lines = f.readlines()
# #print(lines)
# name = Array(100,LinkedList())
# posX = Array(100,LinkedList())
# posY = Array(100,LinkedList())
# dir = Array(100,LinkedList())
# cont=-1
# line=1
# for line in lines:
#     switch = 0
#     cont+=1
#     for i in range (line.__len__()):
#         if line.__getitem__(i) == " ":
#             switch+=1
#         else:
#             if switch == 0:
#                 if name[cont] == None:
#                     listNames = LinkedList()
#                     add(listNames,line.__getitem__(i))
#                     name[cont] =listNames
#                 else:
#                     add(name[cont],line.__getitem__(i))
#             elif switch == 1:
#                 if posX[cont] == None:
#                     listPosX = LinkedList()
#                     add(listPosX,line.__getitem__(i))
#                     posX[cont] =listPosX
#                 else:
#                     add(posX[cont],line.__getitem__(i))
#             elif switch == 2:
#                 if posY[cont] == None:
#                     listPosY = LinkedList()
#                     add(listPosY,line.__getitem__(i))
#                     posY[cont] =listPosY
#                 else:
#                     add(posY[cont],line.__getitem__(i))
#             elif switch == 3:
#                 if dir[cont] == None:
#                     listDir = LinkedList()
#                     add(listDir,line.__getitem__(i))
#                     dir[cont] =listDir
#                 else:
#                     add(dir[cont],line.__getitem__(i))
# for i in range(100):
#     printear(name[i])
#     printear(posX[i])
#     printear(posY[i])
#     printear(dir[i])

# f.close()