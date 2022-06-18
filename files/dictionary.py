import copy
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

    def getArray(self,date):
        A = algo1.Array(self.truesize, obj.Ship(None, 0, 0, None))
        j = 0
        for i in range(len(self.data)):
            if self.data[i] != None:
                A[j] = copy.deepcopy(self.data[i])
                tupla = movement(A,date,j)
                A[j].position.x = tupla[0] 
                A[j].position.y = tupla[1] 
                if j == 88751:
                    print(A[j].id,end=" ")
                    print(A[j].direction,end=" ")
                    print(A[j].position.x,end=" ")
                    print(A[j].position.y)
                j += 1
        return A


def movement(A,days,index):
    if algo1.strcmp(A.data[index].direction, algo1.String("NW")):
        return A.data[index].position.x - days, A.data[index].position.y + days

    elif algo1.strcmp(A.data[index].direction, algo1.String("N")):
        return A.data[index].position.x, A.data[index].position.y + days
    
    elif algo1.strcmp(A.data[index].direction, algo1.String("NE")):
        return A.data[index].position.x + days, A.data[index].position.y + days
    
    elif algo1.strcmp(A.data[index].direction, algo1.String("W")):
        return A.data[index].position.x - days, A.data[index].position.y
    
    elif algo1.strcmp(A.data[index].direction, algo1.String("E")):
        return A.data[index].position.x + days, A.data[index].position.y
    
    elif algo1.strcmp(A.data[index].direction, algo1.String("SW")):
        return A.data[index].position.x - days, A.data[index].position.y - days

    elif algo1.strcmp(A.data[index].direction, algo1.String("S")):
        return A.data[index].position.x, A.data[index].position.y - days

    elif algo1.strcmp(A.data[index].direction, algo1.String("SE")):
        return A.data[index].position.x + days, A.data[index].position.y - days