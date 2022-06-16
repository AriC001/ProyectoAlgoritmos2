def QuickSort(A, p, r):
    if p<r:
        q = partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)


def partition(A,p,r):
    i = p-1
    for j in range(p,r):
        if A[j].position.x <= A[r].position.x:
            i += 1
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    aux = A[i+1]
    A[i+1] = A[r]
    A[r] = aux
    return i+1