import objects as obj
import dictionary as dict
import algo1 as algo1
import navigation_system as ns

dictionary = ns.create()

index = dictionary.search(obj.getKey("barco1"))

if index:
    print(dictionary.data[index])
    print(ns.search(dictionary, "barco1", "15/xx"))