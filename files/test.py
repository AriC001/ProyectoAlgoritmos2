import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray
import objects as objects
import algo1 as algo1

'''create from txt'''
# D = ns.create()

'''create from binary'''
D = ns.create2()


'''-search <date> <nombre_embarcacion>'''
print(ns.search(D, "01/05/2022", "barco85"))
print(ns.search(D, "01/05/2022", "barco36"))
print(ns.closer(D,"01/05/2022"))


'''navigation_system.py -closer <date>'''
C = ns.closer(D,"01-05-2022")
print(C)


'''navigation_system.py -closer <date>'''
ns.collision(D)


