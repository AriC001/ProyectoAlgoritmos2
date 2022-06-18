import navigation_system as ns
import linkedlist as linkedlist
import dictionary as dict
import myarray as myarray

D = ns.create()
print("---------------------------------")
R = ns.closer(D)
curr = R.head
for i in range(3):
    print(curr.value)
    curr = curr.nextNode