import navigation_system2 as ns
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
#print(ns.search(D, "01/05/2022", "b85"))
#print(ns.search(D, "01/05/2022", "b36"))


'''navigation_system.py -closer <date>'''
C = ns.closer("01-05-2022")
print(C)


'''navigation_system.py -closer <date>'''
#ns.collision()


