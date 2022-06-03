import algo1 as algo1
import objects as obj
import prime as prime

class Dictionary:

    def __init__(self, size):
        self.data = algo1.Array(prime.nextPrime(size*2), obj.Ship(None, None, None, None))
        self.prime = prime.prevPrime(size)

    def __len__(self):
        return len(self.data)
        
    def insert(self, ship):
        inserted = False
        i = 0
        while not inserted:
            if self.data[self.doublehash(ship.key, i)] == None:
                self.data[self.doublehash(ship.key, i)] = ship
                inserted = True
                if inserted and i!=0:
                    print(ship, "collisions", i)
            i+=1

    def hash1(self, key):
        return key%len(self)

    def hash2(self, key):
        return self.prime-(key%self.prime)

    def doublehash(self, key, i):
        return (self.hash1(key)+i*self.hash2(key))%len(self)

    def search(self, key):
        found = False
        i = 0
        while not found:

            if self.data[self.doublehash(key, i)] == None:
                return None
            
            if self.data[self.doublehash(key, i)].key == key:
                return self.doublehash(key, i)
            i+=1
    def movement(self,key,date):
        days = float(date.__getitem__(0)) * 10 + int(date.__getitem__(1))
        if str(self.data[key].direction) == "NW":
            self.data[key].position.x += days
            self.data[key].position.y += days
        
        elif str(self.data[key].direction) == "NE":
            self.data[key].position.x -= days
            self.data[key].position.y += days
        
        elif str(self.data[key].direction) == "SW":
            self.data[key].position.x += days
            self.data[key].position.y -= days

        elif str(self.data[key].direction) == "SE":
            self.data[key].position.x -= days
            self.data[key].position.y -= days
        
        elif str(self.data[key].direction) == "N":
            self.data[key].position.y += days
        
        elif str(self.data[key].direction) == "S":
            self.data[key].position.y -= days

        elif (self.data[key].direction) == "E":
            self.data[key].position.x -= days

        elif str(self.data[key].direction) == "W":
            self.data[key].position.x = self.data[key].position.x + days
        
        print(self.data[key].position.x,end=" ")
        print(self.data[key].position.y)
        return 