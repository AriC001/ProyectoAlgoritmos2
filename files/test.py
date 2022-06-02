import objects as obj
import dictionary as dict

shipDictionary = dict.Dictionary(64)

for i in range(64):
    shipDictionary.insert(obj.Ship("barco"+str(i), 0, 0, "N"))

print("==========================")
for i in range(len(shipDictionary)):
    print(shipDictionary.data[i])

print(shipDictionary.search(obj.getKey("barco64")))
print(shipDictionary.search(obj.getKey("barco1")))