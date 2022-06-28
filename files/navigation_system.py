import sys
import linkedlist as linkedlist
import navigation_system2 as nv


if len(sys.argv) > 1:
  if sys.argv[1] == "-create":
    print(nv.create()) # el argv 2 debería ser el archivo o la ubicación de este
  elif sys.argv[1] == "-search":
    print(nv.search(sys.argv[2],sys.argv[3]))
  elif sys.argv[1] == "-closer":
    print(nv.closer(sys.argv[2]))
  elif sys.argv[1] == "-collision":
    C = nv.collision()
    print(C)
    if C != False:
        print("Colisiones Totales = ",linkedlist.length(C))
  else:
    print ("Error")