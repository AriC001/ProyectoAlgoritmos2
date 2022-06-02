import objects as obj
import dictionary as dict
import algo1 as algo1
import navigation_system as ns

dictionary = ns.create()

print("==========================")
for i in range(len(dictionary)):
    if dictionary.data[i] != None:
        print(dictionary.data[i])