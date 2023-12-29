class LinkedList:

    head = None

    def __str__(self):
        currentNode = self.head
        string = "["
        while currentNode != None:
            string += currentNode.value.__str__()
            currentNode = currentNode.nextNode
            if currentNode != None:
                string += ", "
                string += "\n"
        string += "]"
        return string


class Node:

    value = None
    nextNode = None


def add(L, element):

    if L == None:
        return

    newNode = Node()
    newNode.value = element
    newNode.nextNode = L.head
    L.head = newNode


def length(L):

    if L == None:
        return 0

    elements = 0
    currentNode = L.head

    while currentNode != None:
        elements += 1
        currentNode = currentNode.nextNode

    return elements


def access(L, position):

    if L == None:
        return

    if position == None:
        return

    if position < 0:
        return

    if position >= length(L):
        return

    currentNode = L.head

    for i in range(position):
        currentNode = currentNode.nextNode

    return currentNode.value


def addInverted(L, element):

    if L == None:
        newNode = Node()
        newNode.value = element
        L.head = newNode
    else:
        newNode = Node()
        current = Node()
        current = L.head
        newNode.value = element
        while current != None:
            current = current.nextNode
        current = newNode
