from algo1 import *
from main import *

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

        
class Ship:

    def __init__(self, id, x, y, direction):
        self.id = id
        self.position = Position(x, y)
        self.direction = direction
        self.xorder = 0
        self.yorder = 0

    def __str__(self):
        return "{"+str(self.id)+", "+self.position.__str__()+", "+str(self.direction)+"}"

    def movement(self, date, firstDay):
        days = getDays(date) - getDays(firstDay)

        if strcmp(self.direction, String("NW")):
            self.position.x -= days
            self.position.y += days
        
        elif strcmp(self.direction, String("N")):
            self.position.y += days

        elif strcmp(self.direction, String("NE")):
            self.position.x += days
            self.position.y += days

        elif strcmp(self.direction, String("W")):
            self.position.x -= days

        elif strcmp(self.direction, String("E")):
            self.position.x += days

        elif strcmp(self.direction, String("SW")):
            self.position.x -= days
            self.position.y -= days

        elif strcmp(self.direction, String("S")):
            self.position.y -= days

        elif strcmp(self.direction, String("SE")):
            self.position.x += days
            self.position.y -= days

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

    def __str__(self):
        return "{ "+self.ship1.__str__()+", "+self.ship2.__str__()+", "+str(self.distance)+"}"

class CollisionRisk:

    def __init__(self, s1, s2, day):
        self.ship1 = Ship(s1.id, s1.position.x, s1.position.y, s1.direction)
        self.ship2 = Ship(s2.id, s2.position.x, s2.position.y, s2.direction)
        self.day = day

    def __str__(self):
        return "{ "+self.ship1.__str__()+", "+self.ship2.__str__()+", "+str(self.day)+"}"