import objects as obj
import dictionary as dict
import algo1 as algo1
import navigation_system as ns

dictionary = ns.create()

index = dictionary.search(obj.getKey("barco27"),"barco27")
print(index)
if index:
    print(dictionary.data[index])
    print(ns.search(dictionary, "barco27", "15/xx"))