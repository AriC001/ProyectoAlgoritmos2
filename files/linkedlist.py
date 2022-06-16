class LinkedList:

    head = None

    def __str__(self):
        currentNode = self.head
        string = "["
        while currentNode != None:
            string += currentNode.value
            currentNode = currentNode.nextNode
            if currentNode != None:
                string += ", "
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

def getMiddleNode(head):
    middleNode = head
    lastNode = head
    while lastNode.nextNode:
        if lastNode.nextNode.nextNode:
            middleNode = middleNode.nextNode
            lastNode = lastNode.nextNode.nextNode
        else:
            return middleNode
    return middleNode


def merge(head1, head2):
    currentNode = Node()
    auxPointer = currentNode
    while head1 and head2:
        if head1.value.position.y < head2.value.position.y:
            currentNode.nextNode = head1
            head1 = head1.nextNode
        else:
            currentNode.nextNode = head2
            head2 = head2.nextNode
        currentNode = currentNode.nextNode
    if head1:
        currentNode.nextNode = head1
    else:
        currentNode.nextNode = head2
    return auxPointer.nextNode


def MergeSortR(head):
    if head:
        if head.nextNode:
            rightSubListHeadPreviousNode = getMiddleNode(head)
            rightSubListHead = rightSubListHeadPreviousNode.nextNode
            rightSubListHeadPreviousNode.nextNode = None
            head = MergeSortR(head)
            rightSubListHead = MergeSortR(rightSubListHead)
            return merge(head, rightSubListHead)
        else:
            return head
    else:
        return head


def mergesort(L):
    L.head = MergeSortR(L.head)