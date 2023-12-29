import myarray as myarray
import linkedlist as linkedlist
import algo1 as algo1
import objects as objects

# Closest pair of points algorithm

# Brute force algorithm


def distance(s1, s2):
    return ((s1.position.x-s2.position.x)**2+(s1.position.y-s2.position.y)**2)**(1/2)


def bfcpop(P, s, e):
    r = linkedlist.LinkedList()
    delta = 2**64-1
    for i in range(s, e):
        for j in range(i+1, e+1):
            if i == j:
                continue
            if distance(P[i], P[j]) < delta:
                s1 = P[i]
                s2 = P[j]
                delta = distance(P[i], P[j])
    return objects.Distance(s1, s2, delta)

# Divide and conquer algorithm


def dnccpop(X, s, e, Y):
    if e-s < 3:
        return bfcpop(X, s, e)

    Yl = algo1.Array((e-s)//2+1, objects.Ship(None, None, None, None, None))
    Yr = algo1.Array((e-s+1)//2, objects.Ship(None, None, None, None, None))
    j = 0
    k = 0
    for i in range(len(Y)):
        if Y[i].xorder <= (s+e)//2:
            Yl[j] = Y[i]
            j += 1
        else:
            Yr[k] = Y[i]
            k += 1

    rl = dnccpop(X, s, (s+e)//2, Yl)

    rr = dnccpop(X, (s+e)//2+1, e, Yr)

    if rl.distance < rr.distance:
        s1 = rl.ship1
        s2 = rl.ship2
        delta = rl.distance
    else:
        s1 = rr.ship1
        s2 = rr.ship2
        delta = rr.distance

    band = linkedlist.LinkedList()

    for i in range(len(Y)-1, -1, -1):
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
                s1 = currentNode.value
                s2 = compareNode.value
                delta = distance(currentNode.value, compareNode.value)

            compareNode = compareNode.nextNode

        currentNode = currentNode.nextNode

    r = objects.Distance(s1, s2, delta)
    return r
