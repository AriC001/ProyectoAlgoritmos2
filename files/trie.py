from algo1 import *

class TrieNode:

    children = None
    ship = None

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.children = Array(63, TrieNode())

    def insert(self, ship):
        
        pCrawl = self.root.children

        for i in range(len(ship.id)):

            index = getInt(ship.id[i])
            if pCrawl[index] == None:
                pCrawl[index] = TrieNode()
            
            if i == len(ship.id)-1:
                pCrawl[index].ship = ship
                return index
            elif pCrawl[index].children == None:
                pCrawl[index].children = Array(63, TrieNode())

            pCrawl = pCrawl[index].children

    def search(self, id):

        pCrawl = self.root.children

        for i in range(len(id)):

            if pCrawl == None:
                return

            index = getInt(id[i])
            if pCrawl[index] == None:
                return
            
            if i == len(id)-1:
                return pCrawl[index].ship

            pCrawl = pCrawl[index].children

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
