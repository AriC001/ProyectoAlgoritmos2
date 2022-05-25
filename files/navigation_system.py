from algo1 import* 
from linkedlist import*

f = open("data/ships.txt","+r")
linea1 = f.readline()
print(linea1)
lines = f.readlines()
#print(lines)
name = Array(100,LinkedList())
posX = Array(100,LinkedList())
posY = Array(100,LinkedList())
dir = Array(100,LinkedList())
cont=-1
line=1
for line in lines:
    switch = 0
    cont+=1
    for i in range (line.__len__()):
        if line.__getitem__(i) == " ":
            switch+=1
        else:
            if switch == 0:
                if name[cont] == None:
                    listNames = LinkedList()
                    add(listNames,line.__getitem__(i))
                    name[cont] =listNames
                else:
                    add(name[cont],line.__getitem__(i))
            elif switch == 1:
                if posX[cont] == None:
                    listPosX = LinkedList()
                    add(listPosX,line.__getitem__(i))
                    posX[cont] =listPosX
                else:
                    add(posX[cont],line.__getitem__(i))
            elif switch == 2:
                if posY[cont] == None:
                    listPosY = LinkedList()
                    add(listPosY,line.__getitem__(i))
                    posY[cont] =listPosY
                else:
                    add(posY[cont],line.__getitem__(i))
            elif switch == 3:
                if dir[cont] == None:
                    listDir = LinkedList()
                    add(listDir,line.__getitem__(i))
                    dir[cont] =listDir
                else:
                    add(dir[cont],line.__getitem__(i))
for i in range(100):
    printear(name[i])
    printear(posX[i])
    printear(posY[i])
    printear(dir[i])

f.close()