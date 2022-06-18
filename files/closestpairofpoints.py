import myarray as myarray
import linkedlist as linkedlist
import algo1 as algo1
import objects as objects

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
    linkedlist.add(r, delta)
    linkedlist.add(r, s2)
    linkedlist.add(r, s1)
    return r

#Divide and conquer algorithm
def dnccpop(D):
    P = D.getArray()
    Y = D.getArray()
    myarray.QuickSortX(P,0,len(P)-1)
    myarray.QuickSortY(Y,0,len(P)-1)
    return dnccpopr(P,0,len(P),Y)

def dnccpopr(X,s,e,Y):
    if e-s <= 3:
        return bfcpop(X,s,e)

    Yl = algo1.Array((s+e)//2-s, objects.Ship(None, 0, 0, None))
    Yr = algo1.Array(e-(s+e)//2, objects.Ship(None, 0, 0, None))
    j = 0
    k = 0
    for i in range(len(Y)):
        if Y[i].order < (s+e)//2:
            Yl[j] = Y[i]
            j += 1
        else:
            Yr[k] = Y[i]
            k += 1

    rl = dnccpopr(X,s,(s+e)//2,Yl)

    rr = dnccpopr(X,(s+e)//2,e,Yr)

    if linkedlist.access(rl,2) < linkedlist.access(rr,2):
        curr = rl.head
        s1 = curr.value
        curr = curr.nextNode
        s2 = curr.value
        curr = curr.nextNode
        delta = curr.value
    else:
        curr = rr.head
        s1 = curr.value
        curr = curr.nextNode
        s2 = curr.value
        curr = curr.nextNode
        delta = curr.value
        
    band = linkedlist.LinkedList()

    for i in range(len(Y)-1, -1, -1):
        if X[e//2].position.x-delta < Y[i].position.x and X[e//2].position.x+delta > Y[i].position.x:
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
                s1 = currentNode.value
                s2 = compareNode.value
                delta = distance(currentNode.value, compareNode.value)

            compareNode = compareNode.nextNode

        currentNode = currentNode.nextNode

    r = linkedlist.LinkedList()
    linkedlist.add(r,delta)
    linkedlist.add(r,s2)
    linkedlist.add(r,s1)
    return r