import prime as prime

class Position:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


class Ship:
    
    def __init__(self, id, x, y, direction):
        self.id = id
        self.key = getKey(id)
        self.position = Position(x, y)
        self.direction = direction

    def __str__(self):
        return "{"+str(self.id)+", "+self.position.__str__()+", "+str(self.direction)+"}"

def getInt(character):
    unicode = ord(character)
    if unicode == 45:
        return 0
    if unicode >= 48 and unicode <= 57:
        return unicode-47
    if unicode >= 65 and unicode <= 90:
        return unicode-54
    if unicode >= 97 and unicode <= 122:
        return unicode-60

def getKey(id):
    if id == None:
         return None
    k = 0
    for i in range(len(id)):
        k += getInt(id[i])*63**i

    return k