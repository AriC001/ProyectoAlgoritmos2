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
        self.position = Position(x, y, date)
        self.direction = direction
        self.xorder = None

    def __str__(self):
        return "{"+str(self.id)+", "+self.position.__str__()+", "+str(self.direction)+"}"

    def movement(self, date):
        days = getDays(date)-getDays(self.position.date)
        self.position.date = date

        if algo1.strcmp(self.direction, algo1.String("NW")):
            self.position.x -= days
            self.position.y += days
        
        elif algo1.strcmp(self.direction, algo1.String("N")):
            self.position.y += days

        elif algo1.strcmp(self.direction, algo1.String("NE")):
            self.position.x += days
            self.position.y += days

        elif algo1.strcmp(self.direction, algo1.String("W")):
            self.position.x -= days

        elif algo1.strcmp(self.direction, algo1.String("E")):
            self.position.x += days

        elif algo1.strcmp(self.direction, algo1.String("SW")):
            self.position.x -= days
            self.position.y -= days

        elif algo1.strcmp(self.direction, algo1.String("S")):
            self.position.y -= days

        elif algo1.strcmp(self.direction, algo1.String("SE")):
            self.position.x += days
            self.position.y -= days

def getDays(date):
    d = 0
    for i in range(2):
        d *= 10
        d += ord(date[i])-48
    return d

def strToInt(s):
    n = 0
    for i in range(len(s)):
        n *= 10
        n += int(s[i])
    return n

class Distance:

    def __init__(self, s1, s2, d):
        self.ship1 = s1
        self.ship2 = s2
        self.distance = d

    def __str__(self):
        return "{ "+self.ship1.__str__()+", "+self.ship2.__str__()+", "+str(self.distance)+"}"

class CollisionRisk:

    def __init__(self, s1, s2, day):
        self.ship1 = Ship(s1.id, s1.position.x, s1.position.y, s1.position.date, s1.direction)
        self.ship2 = Ship(s2.id, s2.position.x, s2.position.y, s2.position.date, s2.direction)
        self.day = day

    def __str__(self):
        return "{ "+self.ship1.__str__()+", "+self.ship2.__str__()+", "+str(self.day)+"}"