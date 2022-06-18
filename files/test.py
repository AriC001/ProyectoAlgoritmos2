import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray


D = ns.create()
R1 = ns.closer(D, "01/xx/xxxx")
R2 = ns.closer(D, "02/xx/xxxx")
print(R1)
print(R2)


# dictionary = ns.create2()

# #-search <date> <nombre_embarcacion>
# print(ns.search(dictionary,"01-05-2022","barco0"))

# #navigation_system.py -closer <date>
# list = ns.closer(dictionary,"01-05-2022")
# curr = list.head
# for i in range(3):
#     print(curr.value)
#     curr = curr.nextNode

