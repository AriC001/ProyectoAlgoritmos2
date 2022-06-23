import objects as obj
import dictionary as dict
import algo1 as algo1
import linkedlist as linkedlist
import closestpairofpoints as cpop
import pickle

def create():
    with open("data/ships.txt", "r") as file:
        lines = file.readlines()
        lslen = len(lines)
        dictionary = dict.Dictionary((lslen-1))
        date = lines[0]
        for i in range(1, lslen):
            attrno = 0
            llen = len(lines[i])
            for j in range(llen):

                if algo1.strcmp(lines[i][j], " ") and attrno == 0:
                    id = algo1.substr(lines[i], 0, j)
                    start = j+1
                    attrno += 1

                elif algo1.strcmp(lines[i][j], " ") and attrno == 1:
                    x = algo1.substr(lines[i], start, j)
                    start = j+1
                    attrno += 1

                elif algo1.strcmp(lines[i][j], " ") and attrno == 2:
                    y = algo1.substr(lines[i], start, j)
                    start = j+1
                    attrno += 1

                elif j == llen-1:
                    direction = algo1.substr(lines[i], start, j)

            dictionary.insert(obj.Ship(id, toFloat(x), toFloat(y), date, direction))
        with open("data/trieShips", "bw") as f:
            pickle.dump(dictionary,f)
    return dictionary

def toFloat(s):
    ip = 0
    dp = 0
    m = 1
    pi = len(s)
    for i in range(len(s)):
        if i == 0 and algo1.strcmp(s[i], "-"):
            m = -1
        elif algo1.strcmp(s[i], "."):
            pi = i
        elif i < pi:
            ip *= 10
            ip += ord(s[i])-48
        elif i > pi:
            dp *= 10
            dp += ord(s[i])-48
    dp /= 10**(len(s)-pi-1)
    return m*(ip+dp)

def create2():
    with open("data/trieShips", "br") as f:
        file = open("data/ships.txt", "r")
        lines = file.readlines()
        lslen = len(lines)
        dictionary2 = dict.Dictionary((lslen-1))
        dictionary2 = pickle.load(f)
    return dictionary2

def search(dictionary, date, id):

    index = dictionary.search(id)

    if not index:
        return None

    days = obj.getDays(date)-obj.getDays(dictionary.data[index].position.date)

    if algo1.strcmp(dictionary.data[index].direction, algo1.String("NW")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y + days, date)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("N")):
        return obj.Position(dictionary.data[index].position.x, dictionary.data[index].position.y + days, date)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("NE")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y + days, date)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("W")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y, date)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("E")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y, date)
    
    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("SW")):
        return obj.Position(dictionary.data[index].position.x - days, dictionary.data[index].position.y - days, date)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("S")):
        return obj.Position(dictionary.data[index].position.x, dictionary.data[index].position.y - days, date)

    elif algo1.strcmp(dictionary.data[index].direction, algo1.String("SE")):
        return obj.Position(dictionary.data[index].position.x + days, dictionary.data[index].position.y - days, date)


def closer(D, date):
    r = algo1.Array(2, algo1.String(""))
    cp = cpop.dnccpop(D, date)
    r[0] = cp.ship1.id
    r[1] = cp.ship2.id
    return r