import myarray as myarray
import linkedlist as linkedlist

#Closest pair of points algorithm

#Brute force algorithm
def distance(s1, s2):
    return ((s1.x-s2.x)**2+(s1.y-s2.y)**2)**(1/2)

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
def dnccpop(P):
    myarray.QuickSort(P,0,len(P)-1)
    return dnccpopr(P,0,len(P))

def dnccpopr(X,s,e):
    if e-s <= 3:
        return bfcpop(X,s,e)

    r1 = dnccpopr(X,s,(s+e)//2)

    r2 = dnccpopr(X,(s+e)//2,e)

    r = linkedlist.LinkedList()

    if linkedlist.access(r1,2) < linkedlist.access(r2,2):
        curr = r1.head
        s1 = curr.value
        curr = curr.nextNode
        s2 = curr.value
        curr = curr.nextNode
        delta = curr.value
    else:
        curr = r2.head
        s1 = curr.value
        curr = curr.nextNode
        s2 = curr.value
        curr = curr.nextNode
        delta = curr.value
        
    band = linkedlist.LinkedList()
    linkedlist.add(band, X[e//2])

    i = e//2-1
    while i > -1 and i < len(X):
        if X[e//2].position.x-delta < X[i].position.x:
            linkedlist.add(band, X[i])
            i -= 1
        else:
            break
    i = e//2+1
    while i > -1 and i < len(X):
        if X[e//2].position.x+delta > X[i].position.x:
            linkedlist.add(band, X[i])
            i += 1
        else:
            break

    linkedlist.mergesort(band)

    currentNode = band.head
    while currentNode != None:
        compareNode = currentNode.nextNode
        for i in range(7):

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