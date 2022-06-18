import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray


#dictionary = ns.create()

dictionary = ns.create2()

list = ns.closer(dictionary)
curr = list.head
for i in range(3):
    print(curr.value)
    curr = curr.nextNode

