from algo1 import *
from objects import *
from random import *

def swapX(A, i, j):
    if i==j:
        return
    aux = A[i]
    A[i] = A[j]
    A[j] = aux
    A[i].xorder = i
    A[j].xorder = j

def swapY(A, i, j):
    if i==j:
        return
    aux = A[i]
    A[i] = A[j]
    A[j] = aux
    A[i].yorder = i
    A[j].yorder = j

def medianX(A, p, r):
    if A[p].position.x > A[(p+r)//2].position.x or A[p].position.x == A[(p+r)//2].position.x and A[p].position.y > A[(p+r)//2].position.y:
        swapX(A, p, (p+r)//2)
    if A[(p+r)//2].position.x > A[r].position.x or A[(p+r)//2].position.x == A[r].position.x and A[(p+r)//2].position.y > A[r].position.y:
        swapX(A, (p+r)//2, r)
    if A[p].position.x > A[(p+r)//2].position.x or A[p].position.x == A[(p+r)//2].position.x and A[p].position.y > A[(p+r)//2].position.y:
        swapX(A, p, (p+r)//2)

def medianY(A, p, r):
    if A[p].position.y > A[(p+r)//2].position.y or A[p].position.y == A[(p+r)//2].position.y and A[p].position.x > A[(p+r)//2].position.x:
        swapY(A, p, (p+r)//2)
    if A[(p+r)//2].position.y > A[r].position.y or A[(p+r)//2].position.y == A[r].position.y and A[(p+r)//2].position.x > A[r].position.x:
        swapY(A, (p+r)//2, r)
    if A[p].position.y > A[(p+r)//2].position.y or A[p].position.y == A[(p+r)//2].position.y and A[p].position.x > A[(p+r)//2].position.x:
        swapY(A, p, (p+r)//2)

def quickSortX(A, p, r):
    if p<r:
        q = partitionX(A, p, r)
        quickSortX(A, p, q-1)
        quickSortX(A, q+1, r)

def partitionX(A, p, r):
    i = p
    medianX(A, p, r)
    if r-p<3:
        return (p+r)//2
    swapX(A, (p+r)//2, r-1)
    for j in range(p+1,r-1):
        if A[j].position.x < A[r-1].position.x or A[j].position.x == A[r-1].position.x and A[j].position.y <= A[r-1].position.y:
            i += 1
            swapX(A, i, j)
    swapX(A, i+1, r-1)
    return i+1

def quickSortY(A, p, r):
    if p<r:
        q = partitionY(A, p, r)
        quickSortY(A, p, q-1)
        quickSortY(A, q+1, r)

def partitionY(A, p, r):
    i = p
    medianY(A, p, r)
    if r-p<3:
        return (p+r)//2
    swapY(A, (p+r)//2, r-1)
    for j in range(p+1,r-1):
        if A[j].position.y < A[r-1].position.y or A[j].position.y == A[r-1].position.y and A[j].position.x <= A[r-1].position.x:
            i += 1
            swapY(A, i, j)
    swapY(A, i+1, r-1)
    return i+1

def copyArray(A):
    B = Array(len(A), Ship(None, None, None, None))
    for i in range(len(A)):
        B[i] = Ship(A[i].id, A[i].position.x, A[i].position.y, A[i].direction)
        B[i].xorder = A[i].xorder
        B[i].yorder = A[i].yorder
    return B

def deleteX(A, index):
    B = Array(len(A)-1, Ship(None, None, None, None))
    j = 0
    y = A[index].yorder
    for i in range(len(A)):
        if A[i].xorder != index:
            B[j] = A[i]
            if index < A[i].xorder:
                B[j].xorder -= 1
            if y < A[i].yorder:
                B[j].yorder -= 1
            j+=1
    return B

def deleteY(A, index):
    B = Array(len(A)-1, Ship(None, None, None, None))
    j = 0
    x = A[index].xorder
    for i in range(len(A)):
        if A[i].yorder != index:
            B[j] = A[i]
            if x < A[i].xorder:
                B[j].xorder -= 1
            if index < A[i].yorder:
                B[j].yorder -= 1
            j+=1
    return B