import algo1 as algo1
import objects as obj
import prime as prime
import myarray as myarray


class Dictionary:

    def __init__(self, size):
        self.data = algo1.Array(prime.nextPrime(
            2*size), DictionaryNode(None, None))
        self.prime = prime.prevPrime(len(self))
        self.truesize = 0

    def __len__(self):
        return len(self.data)

    def insert(self, ship):
        i = 0
        key = getKey(ship.id)
        while True:
            index = self.doublehash(key, i)
            if self.data[index] == None:
                self.data[index] = DictionaryNode(ship, key)
                self.truesize += 1
                return index
            if self.data[index].key == -1:
                self.data[index] = DictionaryNode(ship, key)
                self.truesize += 1
                return index
            i += 1

    def hash1(self, key):
        return key % len(self)

    def hash2(self, key):
        return self.prime-(key % self.prime)

    def doublehash(self, key, i):
        return (self.hash1(key)+i*self.hash2(key)) % len(self)

    def search(self, id):
        key = getKey(id)
        i = 0
        while True:
            index = self.doublehash(key, i)
            if self.data[index] == None:
                return None
            if self.data[index].key == key:
                return index
            i += 1

    def getArray(self):
        A = algo1.Array(self.truesize, obj.Ship(None, None, None, None, None))
        j = 0
        for i in range(len(self.data)):
            if self.data[i] != None:
                if self.data[i].key > -1:
                    A[j] = obj.Ship(self.data[i].value.id, self.data[i].value.position.x,
                                    self.data[i].value.position.y, self.data[i].value.position.date, self.data[i].value.direction)
                    j += 1
        return A

    def copy(self):
        D = Dictionary(self.truesize)
        for i in range(len(D.data)):
            if D.data[i] != None:
                if D.data[i].key > -1:
                    D.insert(obj.Ship(D.data[i].id, D.data[i].position.x,
                             D.data[i].position.y, D.data[i].position.date, D.data[i].direction))
        return D

    def delete(self, id):
        key = getKey(id)
        i = 0
        while True:
            index = self.doublehash(key, i)
            if self.data[index] == None:
                return None
            if self.data[index].key == key:
                self.data[index].key = -1
                self.truesize -= 1
                return index
            i += 1


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


class DictionaryNode:

    def __init__(self, value, key):
        self.value = value
        self.key = key
