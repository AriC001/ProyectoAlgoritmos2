class LinkedList:
    head = None
class Node:
    value = None
    nextNode=None

def add(L,element):
  nodo = Node()
  nodo.value = element
  Current = Node()
  Current = L.head
  if L.head == None:
    L.head = nodo
  else:
    while Current.nextNode != None:
      Current = Current.nextNode
    Current.nextNode = nodo
  return L

def printear(L):
    current=Node()
    current = L.head
    while current != None:
        print(current.value,end="")
        current = current.nextNode
    print()