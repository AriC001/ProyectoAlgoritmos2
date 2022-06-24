import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray
import objects as objects
import algo1 as algo1


# D = ns.create()
D = ns.create2()
print(ns.search(D, "01/05/2022", "barco85"))
print(ns.search(D, "01/05/2022", "barco36"))
print(ns.closer(D,"01/05/2022"))
ns.collision(D)
# #-search <date> <nombre_embarcacion>
# print(ns.search(D,"01-05-2022","barco0"))

# # #navigation_system.py -closer <date>
# C = ns.closer(D,"01-05-2022")
# print(C)


# ns.collision(D)

