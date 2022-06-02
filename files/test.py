import objects as obj
import dictionary as dict

shipDictionary = dict.Dictionary(64)

print(len(shipDictionary))
print(shipDictionary.prime)
for i in range(64):
    shipDictionary.insert(obj.Ship("barco"+str(i), 0, 0, "N"))

print("==========================")

print(shipDictionary.search(obj.getKey("barco64")))
print(shipDictionary.search(obj.getKey("barco1")))for i in range(len(shipDictionary)):
    print(shipDictionary.data[i])