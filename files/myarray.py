def QuickSortX(A, p, r):
    if p<r:
        q = partitionX(A,p,r)
        QuickSortX(A,p,q-1)
        QuickSortX(A,q+1,r)


def partitionX(A,p,r):
    i = p-1
    for j in range(p,r):
        if A[j].position.x <= A[r].position.x:
            i += 1
            aux = A[i]
            A[i] = A[j]
            A[i].order = i
            A[j] = aux
            A[j].order = j
    aux = A[i+1]
    A[i+1] = A[r]
    A[i+1].order = i+1
    A[r] = aux
    A[r].order = r
    return i+1

def QuickSortY(A, p, r):
    if p<r:
        q = partitionY(A,p,r)
        QuickSortY(A,p,q-1)
        QuickSortY(A,q+1,r)


def partitionY(A,p,r):
    i = p-1
    for j in range(p,r):
        if A[j].position.y <= A[r].position.y:
            i += 1
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    aux = A[i+1]
    A[i+1] = A[r]
    A[r] = aux
    return i+1