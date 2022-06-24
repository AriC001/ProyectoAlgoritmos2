import prime as prime
import algo1 as algo1

class Position:

    def __init__(self, x, y, date):
        self.x = x
        self.y = y
        self.date = date
        
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

        
class Ship:

    def __init__(self, id, x, y, date, direction):
        self.id = id
        self.key = getKey(id)
        self.position = Position(x, y, date)
        self.direction = direction
        self.xorder = None

    def __str__(self):
        return "{"+str(self.id)+", "+self.position.__str__()+", "+str(self.direction)+"}"

    def movement(self, date):
        days = getDays(date)-getDays(self.position.date)
        self.position.date = date

        if algo1.strcmp(self.direction, algo1.String("NW")):
            self.position.x -= days/2**(1/2)
            self.position.y += days/2**(1/2)
        
        elif algo1.strcmp(self.direction, algo1.String("N")):
            self.position.y += days

        elif algo1.strcmp(self.direction, algo1.String("NE")):
            self.position.x += days/2**(1/2)
            self.position.y += days/2**(1/2)

        elif algo1.strcmp(self.direction, algo1.String("W")):
            self.position.x -= days

        elif algo1.strcmp(self.direction, algo1.String("E")):
            self.position.x += days

        elif algo1.strcmp(self.direction, algo1.String("SW")):
            self.position.x -= days/2**(1/2)
            self.position.y -= days/2**(1/2)

        elif algo1.strcmp(self.direction, algo1.String("S")):
            self.position.y -= days

        elif algo1.strcmp(self.direction, algo1.String("SE")):
            self.position.x += days/2**(1/2)
            self.position.y -= days/2**(1/2)

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
        k += getInt(id[i])*67**i
    return k

def getDays(date):
    d = 0
    for i in range(2):
        d *= 10
        d += ord(date[i])-48
    return d
    
class Distance:

    def __init__(self, s1, s2, d):
        self.ship1 = s1
        self.ship2 = s2
        self.distance = d

class CollisionRisk:

    def __init__(self, s1, s2, day):
        self.ship1 = s1
        self.ship2 = s2
        self.day = day