from objects import *
from algo1 import *
from myarray import *
from linkedlist import *
from trie import *
import pickle

def create():
    with open("../data/ships.txt", "r") as file:
        lines = file.readlines()
        c = countShips(lines)
        T = Trie()
        A = Array(c, Ship(None, None, None, None))
        for i in range(1, c+1):
            attrno = 0
            lineslen = len(lines[i])
            for j in range(lineslen):

                if strcmp(lines[i][j], " ") and attrno == 0:
                    id = substr(lines[i], 0, j)
                    start = j+1
                    attrno += 1

                elif strcmp(lines[i][j], " ") and attrno == 1:
                    x = substr(lines[i], start, j)
                    start = j+1
                    attrno += 1

                elif strcmp(lines[i][j], " ") and attrno == 2:
                    y = substr(lines[i], start, j)
                    start = j+1
                    attrno += 1

                elif j == lineslen-1:
                    direction = substr(lines[i], start, j)

            T.insert(Ship(id, strToInt(x), strToInt(y), direction))
            A[i-1] = Ship(id, strToInt(x), strToInt(y), direction)
            A[i-1].xorder = i-1
            A[i-1].yorder = i-1
        with open("../data/TrieShips", "bw") as f:
            pickle.dump(T,f)
        with open("../data/ArrayShips", "bw") as f:
            pickle.dump(A,f)
    return True

def countShips(lines):
    c = 0
    for i in range(1, len(lines)):
        if len(lines[i]) > 1:
            c += 1
    return c

def firstDay():
    with open("../data/ships.txt", "r") as file:
        s = file.readline()
        return substr(String(s),0,len(s)-1)

def search(date, id):
    with open("../data/TrieShips", "br") as f:
        T = pickle.load(f)

    s = T.search(id)

    if s == None:
        return None

    s.movement(date, firstDay())

    return s.position

def closer(date):
    with open("../data/ArrayShips", "br") as f:
        X = pickle.load(f)
    C = LinkedList()
    c = 2**64
    quickSortX(X,0,len(X)-1)
    Y = copyArray(X)
    quickSortY(Y,0,len(Y)-1)
    for i in range(len(X)):
        X[i].movement(date, firstDay())
    while True:
        cp = dnccpop(X,0,len(X)-1,Y)
        if cp.distance > c:
            break
        c = cp.distance
        add(C, Distance(cp.ship1, cp.ship2, c))
        for i in range(len(X)):
            if i==cp.ship1.xorder or i==cp.ship2.xorder:
                continue
            d = distance(cp.ship1, X[i])
            if d==c:
                add(C, Distance(cp.ship1, X[i], d))
            d = distance(cp.ship2, X[i])
            if d==c:
                add(C, Distance(cp.shiip2, X[i], d))
        X = deleteX(X, cp.ship1.xorder)
        X = deleteX(X, cp.ship2.xorder)
        Y = deleteY(Y, cp.ship1.yorder)
        Y = deleteY(Y, cp.ship2.yorder)
    if C.head != None:
        return C

def collision():
    C = LinkedList()
    date = "00/05/2022"
    for i in range(31):
        with open("../data/ArrayShips", "br") as f:
            X = pickle.load(f)
        Y = copyArray(X)
        date = nextDay(date)
        for i in range(len(X)):
                X[i].movement(date, firstDay())
        quickSortX(X,0,len(X)-1)
        quickSortY(Y,0,len(Y)-1)
        while True:
            cp = dnccpop(X,0,len(X)-1,Y)
            if cp.distance > 1:
                break
            add(C, CollisionRisk(cp.ship1, cp.ship2, date))
            for i in range(len(X)):
                if i==cp.ship1.xorder or i==cp.ship2.xorder:
                    continue
                if distance(cp.ship1, X[i]) <= 1:
                    add(C, CollisionRisk(cp.ship1, X[i], date))
                if distance(cp.ship2, X[i]) <= 1:
                    add(C, CollisionRisk(cp.ship2, X[i], date))
            X = deleteX(X, cp.ship1.xorder)
            X = deleteX(X, cp.ship2.xorder)
            Y = deleteY(Y, cp.ship1.yorder)
            Y = deleteY(Y, cp.ship2.yorder)
    if C.head != None:
        with open("../collsion.txt", "w") as file:
            file.write("")
        with open("../collsion.txt", "w+") as f:
            nodo = Node()
            nodo = C.head
            while nodo != None:
                f.write(str(nodo.value.ship1.id) + " " + str(nodo.value.ship1.position.x) + " " + str(nodo.value.ship1.position.y) + " / " + str(nodo.value.ship2.id) + " " + str(nodo.value.ship2.position.x) + " " + str(nodo.value.ship2.position.y) + " - " + str(nodo.value.day) + "\n" )
                nodo = nodo.nextNode
        return C
    else:
        return False
   
def nextDay(date):
    my = substr(date,2,len(date))
    d = (ord(date[0])-48)*10+(ord(date[1])-48)+1
    if d<10:
        d = concat(String("0"),String(chr(d+48)))
    else:
        d = concat(String(chr(d//10+48)), String(chr(d%10+48)))
    return concat(d,my)

def distance(s1, s2):
    return ((s1.position.x-s2.position.x)**2+(s1.position.y-s2.position.y)**2)**(1/2)

def bfcpop(P,s,e):
    r = LinkedList()
    delta = 2**64-1
    for i in range(s,e):
        for j in range(i+1,e+1):
            if i == j:
                continue
            if distance(P[i], P[j]) < delta:
                s1 = P[i]
                s2 = P[j]
                delta = distance(P[i], P[j])
    return Distance(s1, s2, delta)

#Divide and conquer algorithm 
def dnccpop(X,s,e,Y):
    if e-s < 3:
        return bfcpop(X,s,e)

    Yl = Array((e-s)//2+1, Ship(None, None, None, None))
    Yr = Array((e-s+1)//2, Ship(None, None, None, None))
    j = 0
    k = 0
    for i in range(len(Y)):
        if Y[i].xorder <= (s+e)//2:
            Yl[j] = Y[i]
            j += 1
        else:
            Yr[k] = Y[i]
            k += 1

    rl = dnccpop(X,s,(s+e)//2,Yl)

    rr = dnccpop(X,(s+e)//2+1,e,Yr)

    if rl.distance < rr.distance:
        s1 = rl.ship1
        s2 = rl.ship2
        delta = rl.distance
    else:
        s1 = rr.ship1
        s2 = rr.ship2
        delta = rr.distance
        
    band = LinkedList()

    for i in range(len(Y)-1, -1, -1):
        if X[(s+e)//2].position.x-delta <= Y[i].position.x and X[(s+e)//2].position.x+delta >= Y[i].position.x:
            add(band, Y[i])

    currentNode = band.head
    while currentNode != None:
        compareNode = currentNode.nextNode
        for i in range(6):

            if compareNode == None:
                break

            if currentNode.value.position.y+delta < compareNode.value.position.y:
                break

            if distance(currentNode.value, compareNode.value) < delta:
                s1 = currentNode.value
                s2 = compareNode.value
                delta = distance(currentNode.value, compareNode.value)

            compareNode = compareNode.nextNode

        currentNode = currentNode.nextNode

    r = Distance(s1, s2, delta)
    return r