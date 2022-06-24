import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray
import objects as objects
import algo1 as algo1


#D = ns.create()
D = ns.create2()
# print(ns.closer(D,"04/xx/xxxx"))

# dictionary = ns.create2()

# #-search <date> <nombre_embarcacion>
print(ns.search(D,"01-05-2022","barco0"))

# #navigation_system.py -closer <date>
list = ns.closer(D,"01-05-2022")
print(list)


ns.collision(D)

