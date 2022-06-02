import prime as prime

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


class Ship:

    def __init__(self, id, x, y, direction):
        self.id = id
        self.key = getKey(id)
        self.position = Position(x, y)
        self.direction = direction

    def __str__(self):
        return "{"+self.id+", "+str(self.key)+", "+self.position.__str__()+", "+self.direction+"}"


def getKey(id):

    if id == None:
        return None

    k = 0
    c = 0
    for i in range(len(id)-1,-1,-1):
        k += ord(id[i])*prime.nextPrime(256)**(c)
        c+=1
    return k