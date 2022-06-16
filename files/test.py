import objects as obj
import dictionary as dict
import algo1 as algo1
import navigation_system as ns

dictionary = ns.create()

print(dictionary.data[dictionary.search("barco12")])
print(ns.search(dictionary,"barco12","15/xx"))

print(dictionary.data[dictionary.search("barco21")])
print(ns.search(dictionary,"barco21","15/xx"))

print(ns.search(dictionary,"barco101","15/xx"))