import os, sys
import shutil
from shutil import copyfile

path = "fitxers"
dirs = os.listdir( path )
 
for file in dirs:
  print (file)
opcio = input("Quin arxiu vols?")
if os.path.exists(path+"/"+opcio):
  fitxer = open(path+"/"+opcio, "r")
  llegir = fitxer.read()
  print(llegir)
else:
  print("L'arxiu demanat no existeix")
  
if llegir[0] == "moure":
  if os.path.exists():
    os.rename(llegir[1], llegir[2])
  else:
    print("L'arxiu demanat no existeix")
elif llegir[0] == "borra":
  os.remove(llegir[1])
elif llegir[0] == "copia":
  copyfile("fitxers/a.txt", "fitxers/x.txt")



