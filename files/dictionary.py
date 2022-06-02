from typing_extensions import Self
import algo1 as algo1
import objects as obj
import prime as prime

class Dictionary:

    def __init__(self, size):
        self.data = algo1.Array(prime.nextPrime(2*size), obj.Ship(None, None, None, None))
        self.prime = prime.prevPrime(size)

    def __len__(self):
        return len(self.data)
        
    def insert(self, ship):
        inserted = False
        i = 0
        while not inserted:
            # if self.data[(ship.key+i)%len(self)] == None:
            #     self.data[(ship.key+i)%len(self)] = ship
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
