import objects as obj
import dictionary as dict
import algo1 as algo1
import navigation_system as ns

dictionary = ns.create()

key = dictionary.search(obj.getKey("barco1"))
if key:
    dictionary.movement(key,"05/05/2022")
