import sys
from linkedlist import *
from main import *


if len(sys.argv) > 1:
  if sys.argv[1] == "-create":
    print(create()) # el argv 2 debería ser el archivo o la ubicación de este
  elif sys.argv[1] == "-search":
    print(search(sys.argv[2],sys.argv[3]))
  elif sys.argv[1] == "-closer":
    C = closer(sys.argv[2])
    print(C)
  elif sys.argv[1] == "-collision":
    C = collision()
    print(C)
    if C != False:
        print("Colisiones Totales = ",length(C))
  else:
    print ("Error")