import objects as obj
import dictionary as dict
import algo1 as algo1
import closestpairofpoints as cpop
import pickle
import myarray as myarray
import linkedlist as linkedlist
import copy


def create():
    with open("data/ships.txt", "r") as file:
        lines = file.readlines()
        ships = getShipCount(lines)
        dictionary = dict.Dictionary((ships))
        date = lines[0]
        for i in range(1, ships+1):
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

def getShipCount(lines):
    c = 0
    for i in range(1, len(lines)):
        if len(lines[i]) > 1:
            c += 1
    return c


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

    s = obj.Ship(dictionary.data[index].id, dictionary.data[index].position.x, dictionary.data[index].position.y, dictionary.data[index].position.date, dictionary.data[index].direction)

    s.movement(date)

    return s.position

def closer(D, date):
    r = algo1.Array(2, algo1.String(""))
    X = D.getArray()
    for i in range(len(X)):
        X[i].movement(date)
    myarray.QuickSortX(X,0,len(X)-1)
    Y = myarray.copy(X)
    myarray.QuickSortY(Y,0,len(Y)-1)
    cp = cpop.dnccpop(X,0,len(X)-1,Y)
    r[0] = cp.ship1.id
    r[1] = cp.ship2.id
    return r

def collision(D):
    
    C = linkedlist.LinkedList()
    date = "00/05/2022"
    for i in range(31):
        Dictionary = copy.deepcopy(D)
        X = Dictionary.getArray()
        date = nextDay(date)
        for i in range(len(X)):
            X[i].movement(date)
        myarray.QuickSortX(X,0,len(X)-1)
        Y = myarray.copy(X)
        myarray.QuickSortY(Y,0,len(Y)-1)
        cp = cpop.dnccpop(X,0,len(X)-1,Y)
        
        while cp.distance <= 1:
            X = Dictionary.getArray()
            for i in range(len(X)):
                X[i].movement(date)
            myarray.QuickSortX(X,0,len(X)-1)
            Y = myarray.copy(X)
            myarray.QuickSortY(Y,0,len(Y)-1)
            cp = cpop.dnccpop(X,0,len(X)-1,Y)

            if cp.distance > 1:
                break

            linkedlist.add(C, obj.CollisionRisk(cp.ship1, cp.ship2, date))
            for i in range(len(X)):
                if i==cp.ship1.xorder or i==cp.ship2.xorder:
                    continue
                if cpop.distance(cp.ship1, X[i]) <= 1:
                    linkedlist.add(C, obj.CollisionRisk(cp.ship1, X[i], date))
                if cpop.distance(cp.ship2, X[i]) <= 1:
                    linkedlist.add(C, obj.CollisionRisk(cp.ship2, X[i], date))
            
            Dictionary.delete(cp.ship1.id)
            Dictionary.delete(cp.ship2.id)

    print(C)
    print(linkedlist.length(C))
    return C

        
        
def nextDay(date):
    my = algo1.substr(date,2,len(date))
    d = (ord(date[0])-48)*10+(ord(date[1])-48)+1
    if d<10:
        d = algo1.concat(algo1.String("0"),algo1.String(chr(d+48)))
    else:
        d = algo1.concat(algo1.String(chr(d//10+48)), algo1.String(chr(d%10+48)))
    return algo1.concat(d,my)