import objects as obj
import dictionary as dict
import algo1 as algo1
import linkedlist as linkedlist
import closestpairofpoints as cpop

def create():
    
    file = open("data/ships.txt", "r")
    lines = file.readlines()
    lslen = len(lines)
    dictionary = dict.Dictionary(lslen-1)
    A = algo1.Array(lslen-1,obj.Ship(None, 0, 0, None))

    for i in range(1, lslen):

        attrno = 0
        llen = len(lines[i])
        for j in range(llen):

            if algo1.strcmp(lines[i][j], " ") and attrno == 0:
                id = algo1.substr(lines[i], 0, j)
                start = j+1
                attrno += 1

            elif algo1.strcmp(lines[i][j], " ") and attrno == 1:
                x1 = algo1.substr(lines[i], start, j)
                x=0
                mult = 1
                for z in range(len(x1)):
                    if algo1.strcmp(x1[z], "-"):
                        mult=-1
                    else:
                        x += int(x1[z])*(10**(len(x1) - (z+1)))
                x = x * mult
                start = j+1
                attrno += 1

            elif algo1.strcmp(lines[i][j], " ") and attrno == 2:
                y1 = algo1.substr(lines[i], start, j)
                y=0
                mult=1
                for v in range(len(y1)):
                    if algo1.strcmp(y1[v], "-"):
                        mult = -1
                    else:
                        y += int(y1[v])*(10**(len(y1) - (v+1)))
                y = y * mult
                start = j+1
                attrno += 1

            elif j == llen-1:
                direction = algo1.substr(lines[i], start, j)

        A[i-1] = obj.Ship(id, x, y, direction)
        dictionary.insert(A[i-1])

    file.close()
    
    R = linkedlist.LinkedList()
    linkedlist.add(R, A)
    linkedlist.add(R, dictionary)
    
    return R


def search(dictionary, id, date):

    days = int(date[0]) * 10 + int(date[1])

    index = dictionary.search(id)

    if not index:
        return

    if algo1.strcmp(dictionary.data[index].direction, algo1.String("NW")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y + days)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("N")):
        return obj.Position(dictionary.data[index].position.x, dictionary.data[index].position.y + days)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("NE")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y + days)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("W")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("E")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("SW")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y - days)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("S")):
        return obj.Position(dictionary.data[index].position.x, dictionary.data[index].position.y - days)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("SE")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y - days)

def closer(A):
    return cpop.dnccpop(A)