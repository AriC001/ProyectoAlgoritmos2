import algo1 as algo1
import objects as objects

class TrieNode:

    children = None
    ship = None

class Trie:

    def __init__(self):
        self.data = algo1.Array(63, TrieNode())

    def insert(self, ship):

        for i in range(len(ship.id)):

            index = getInt(ship.id[i])
            if self.data[index] == None:
                self.data[index] = TrieNode()
            
            if i == len(ship.id)-1:
                self.data[index].ship = ship

    def search(self, id):

        for i in range(len(id)):

            index = getInt(id[i])
            if self.data[index] == None:
                return None
            
            if i == len(id)-1 and self.data[index].ship != None:
                return self.data[index].ship

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