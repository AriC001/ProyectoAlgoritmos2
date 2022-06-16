import navigation_system as ns
import linkedlist as linkedlist

R = ns.create()

# dictionary = linkedlist.access(R,0)

# print(dictionary.data[dictionary.search("barco12")])
# print(ns.search(dictionary,"barco12","15/xx"))

# print(dictionary.data[dictionary.search("barco21")])
# print(ns.search(dictionary,"barco21","15/xx"))

# print(ns.search(dictionary,"barco101","15/xx"))

R2 = ns.closer(linkedlist.access(R,1))

curr = R2.head
for i in range(3):
    print(curr.value)
    curr = curr.nextNode