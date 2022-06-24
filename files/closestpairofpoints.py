import myarray as myarray
import linkedlist as linkedlist
import algo1 as algo1
import objects as objects
import copy

#Closest pair of points algorithm

#Brute force algorithm
def distance(s1, s2):
    return ((s1.position.x-s2.position.x)**2+(s1.position.y-s2.position.y)**2)**(1/2)

def bfcpop(P,s,e):
    r = linkedlist.LinkedList()
    delta = 2**64-1
    for i in range(s,e):
        for j in range(s,e):
            if i == j:
                continue
            if distance(P[i], P[j]) < delta:
                s1 = P[i]
                s2 = P[j]
                delta = distance(P[i], P[j])
    return objects.Distance(s1, s2, delta)

#Divide and conquer algorithm
def dnccpop(D, date,delete):
    P = D.getArray()
    len = trueLen(P)
    for i in range(len):
        if P[i] != None:
            P[i].movement(date)
    myarray.QuickSortX(P,0,len-1)
    Y = myarray.copy(P)
    myarray.QuickSortY(Y,0,len-1)
    return deleteFromD(D,dnccpopr(P,0,len-1,Y),delete)
 
def dnccpopr(X,s,e,Y):
    if e-s <= 3:
        return bfcpop(X,s,e)

    Yl = algo1.Array((e-s)//2+1, objects.Ship(None, None, None, None, None))
    Yr = algo1.Array((e-s+1)//2, objects.Ship(None, None, None, None, None))
    j = 0
    k = 0
    for i in range(trueLen(Y)):
        if Y[i].xorder <= (s+e)//2:
            Yl[j] = Y[i]
            j += 1
        else:
            Yr[k] = Y[i]
            k += 1

    rl = dnccpopr(X,s,(s+e)//2,Yl)

    rr = dnccpopr(X,(s+e)//2+1,e,Yr)

    if rl.distance < rr.distance:
        s1 = rl.ship1
        s2 = rl.ship2
        delta = rl.distance
    else:
        s1 = rr.ship1
        s2 = rr.ship2
        delta = rr.distance
        
    band = linkedlist.LinkedList()

    for i in range(trueLen(Y)-1, -1, -1):
        if X[(s+e)//2].position.x-delta <= Y[i].position.x and X[(s+e)//2].position.x+delta >= Y[i].position.x:
            linkedlist.add(band, Y[i])

    currentNode = band.head
    while currentNode != None:
        compareNode = currentNode.nextNode
        for i in range(6):

            if compareNode == None:
                break

            if currentNode.value.position.y+delta < compareNode.value.position.y:
                break

            if distance(currentNode.value, compareNode.value) < delta:
                s1 = copy.deepcopy(currentNode.value)
                s2 = copy.deepcopy(compareNode.value)
                delta = copy.deepcopy(distance(currentNode.value, compareNode.value))

            compareNode = compareNode.nextNode

        currentNode = currentNode.nextNode

    r = objects.Distance(s1, s2, delta)
    return r

def deleteFromD(D,barcos,delete):
    if delete == 2:
        return D,barcos
    else:
        if delete == 0:
            index = D.search(barcos.ship1.id)
            D.data[index] = objects.Ship(None, None, None, None, None)
        else:
            index = D.search(barcos.ship2.id)
            D.data[index] = objects.Ship(None, None, None, None, None)
        return D,barcos
    

def trueLen(P):
    cont=0
    for i in range(len(P)):
        if P[i] != None:
            cont+=1
    return cont