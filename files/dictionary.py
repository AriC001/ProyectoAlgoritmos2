import algo1 as algo1
import objects as obj
import prime as prime

class Dictionary:

    def __init__(self, size):
        self.data = algo1.Array(prime.nextPrime(int(1.5*size)), obj.Ship(None, 0, 0, None))
        self.prime = prime.prevPrime(size)

    def __len__(self):
        return len(self.data)
        
    def insert(self, ship):
        inserted = False
        i = 0
        while not inserted:
            if i != 0:
                print(i)
            if self.data[self.doublehash(ship.key, i)] == None:
                self.data[self.doublehash(ship.key, i)] = ship
                inserted = True
            i+=1

    def hash1(self, key):
        return key%len(self)

    def hash2(self, key):
        return self.prime-(key%self.prime)

    def doublehash(self, key, i):
        return (self.hash1(key)+i*self.hash2(key))%len(self)

    def search(self, key, id):
        found = False
        i = 0
        while not found:

            if self.data[self.doublehash(key, i)] == None:
                print("",end="")
                #return None
            
            elif algo1.strcmp(self.data[self.doublehash(key, i)].id, id):
                found = True
                return self.doublehash(key, i)
            i+=1