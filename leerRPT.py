"""  
 * Lee el reporte de epanet y lo convierte en un archivo separado por comas o json
 * salen 2 archivos, uno plano y uno en Json.  Verificar si es necesario poner comas
 * para usarse hay que ajustar la cantidad de nudos n
"""
import numpy
import json
import random
import sys

if len(sys.argv) < 2 :   #cuando solo se escribe mgh, imprime el modo de uso y termina
   fin = "armado.rpt"
   fout = "armado.csv"
else:                     #cuando se da el comando más un nombre de archivo, lo ejecuta en modo normal
   fin = sys.argv[1]
   fout = sys.argv[1]
   fout = fout.replace("rpt","csv")
   foutjson = fout.replace("csv","json")
   print(fout)

nudos = []
vars=[]

try:
   f = open(fin,'r')
except:
   print("No pude leer archivo")
   sys.exit()    

orig_stdout = sys.stdout        
f_sal= open(fout,"w")
sys.stdout = f_sal 
contador = -1

with open(fin,'r')  as file:
  while True:
     line = file.readline()
     if not line:
        break
     vars = line.split()
     if (len(vars)>0) and (vars[0] == "Node"):
       contador = contador +1
       for i in range(4):
         line = file.readline()
       while True:
         line = file.readline()
         vars = line.split()
         if (len(vars)==0):
            break
         nudos.append({"hora":contador,"nudo": vars[0], "presion": vars[3]})
         print(f"{contador}, {vars[0]}, {vars[3]} ")
         
json_object = json.dumps(nudos, indent=4)

# Escribir el .json
with open(foutjson, "w") as outfile:
  outfile.write(json_object)
sys.stdout = orig_stdout 
f_sal.close()
file.close()        

#fin CRC