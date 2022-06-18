import algo1 as algo1
import objects as obj
import prime as prime
import myarray as myarray

class Dictionary:

    def __init__(self, size):
        self.data = algo1.Array(prime.nextPrime(2*size), obj.Ship(None, 0, 0, None))
        self.prime = prime.prevPrime(len(self))
        self.truesize = size
        #print(size)

    def __len__(self):
        return len(self.data)
        
    def insert(self, ship):
        inserted = False
        i = 0
        while not inserted:
            if self.data[self.doublehash(ship.key, i)] == None:
                self.data[self.doublehash(ship.key, i)] = ship
                inserted = True
            if inserted and i != 0:
                print("",end="")
                #print(ship)
                #print(str(i)+" collisions")
            i+=1

    def hash1(self, key):
        return key%len(self)

    def hash2(self, key):
        return self.prime-(key%self.prime)

    def doublehash(self, key, i):
        return (self.hash1(key)+i*self.hash2(key))%len(self)

    def search(self, id):
        key = obj.getKey(id)
        found = False
        i = 0
        while not found:

            if self.data[self.doublehash(key, i)] == None:
                return None
            
            if self.data[self.doublehash(key, i)].key == key:
                return self.doublehash(key, i)

            i+=1

    def getArray(self):
        A = algo1.Array(self.truesize, obj.Ship(None, 0, 0, None))
        j = 0
        for i in range(len(self.data)):
            if self.data[i] != None:
                A[j] = self.data[i]
                j += 1
        return A