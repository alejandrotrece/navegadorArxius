import os, sys

path = "fitxers"
dirs = os.listdir( path )
 
for file in dirs:
  print (file)
opcio = input("Quin arxiu vols?")
if os.path.exists(path+"/"+opcio):
  fitxer = open(path+"/"+opcio, "r")
  print(fitxer)
else:
  print("L'arxiu demanat no existeix")