import objects as obj
import dictionary as dict
import algo1 as algo1
import linkedlist as linkedlist
import closestpairofpoints as cpop
import pickle
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
    cp = cpop.dnccpop(D, date,2)
    r[0] = cp[1].ship1.id
    r[1] = cp[1].ship2.id
    return r

def collision(Dictionary):
    mounth = algo1.Array(31,obj.Distance(None,None,None))
    for days in range(30):
        D = copy.deepcopy(Dictionary) #Como se eliminan barcos de D, hay que resetearlo para cada dia
        if days < 9:
            date = "0" + str(days+1)
        else:
            date = str(days+1)
        r = cpop.dnccpop(D, date,0)
        mounth[days] = r[1]
        if mounth[days].distance <= 1:
            print("Day",days+1,": ",mounth[days].ship1.id,mounth[days].ship2.id,mounth[days].distance)
        second = linkedlist.LinkedList()#obj.Distance(None,None,None))
        while mounth[days].distance <= 1:
            #deberia eliminar uno y despues el otro simplemente pasando un numero, ver si es par eliminar uno si es impar eliminar el otro
            r = cpop.dnccpop(D, date,0)
            '''
            D = copy.deepcopy(Dictionary)
            aux = cpop.deleteFromD(D,mounth[days],0)
            D = copy.deepcopy(aux[0])
            '''
            if r[1].distance <= 1:
                linkedlist.addInverted(second,r[1])
                print("Day",days+1,": ",r[1].ship1.id,r[1].ship2.id,r[1].distance)
            mounth[days] = r[1]
        D = copy.deepcopy(Dictionary)
        for j in range(linkedlist.length(second)):
            aux = aux = cpop.deleteFromD(D,second[j].value,1)
            D = copy.deepcopy(aux[0])
            r = cpop.dnccpop(D, date,0)
            if r[1].distance <= 1:
                print("Day",days+1,": ",r[1].ship1.id,r[1].ship2.id,r[1].distance)