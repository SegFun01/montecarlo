"""  
 * Aleatoriamente selecciona valores de caudal demandado de acuerdo con el nivel de probabilidad
   Hace un vector con 100 (o más valores) y luego hace una corrida de Montecarlo
   Para obtener un valor probabilístico del caudal
  Es parte de la modelación, para deninir caudales en los nudos

"""
import numpy
import json
import random
import sys

## Variables globales
n = 10   #----------Este es el número de simulaciones de Montecarlo, usar 1000
f_n= float(n)
qmc=0.0
QT=0.0
random.seed()
dist_frec = []
nudos=[]
c_prob = [(10,0.8),(15, 0.9),(50, 1),(15,1.1),(10,1.2)]
qm = [1.0, 2.0, 3.0, 4.0, 5.0] #caudales de prueba, ya no se usan

def crear_df(c_prob):  # crear la distribución de frecuancias: 100 valores de los cuales escoger
# Se crean 100 valores a partir de los 5 caudales posibles en cantidades de acuerdo a su probabilidad
  df=[]
  for i in range(len(c_prob)):      # esto se realiza las veces requeridas en el periodo extendido
     for j in range(c_prob[i][0]):
        df.append(c_prob[i][1])
  return df      

def obtiene_demanda(df,qm):     #obtener un número aleatorio, obtener la frecuancia respectiva y luego multiplicar por qm
   al = random.randint(0,99)    # al es elo número aleatorio
   qi = qm * df[al]
   return qi


#paso 1  crear la distribución de frecuencias para elegir   
dist_frec = crear_df(c_prob)
  
try:
   f = open('entrada.inp','r')   ## archivo con los nudos de carga originales entrada.inp
except:
   sys.exit()    

#-----Cargar los datos globales de la corrida
encabezados = f.readline().strip()
contador = 0
with open('entrada.inp','r')  as file:  ## archivo con los nudos de carga originales entrada.inp
   for line in file:
      if (contador >=1) : 
        vars = line.split()
        nudos.append(vars)         
      contador = contador + 1

orig_stdout = sys.stdout        

# Realizar la generación n veces
for k in range(n):
   fout = "junctions" + str(k).zfill(3)+".inp"
   print(fout)
   f_sal= open(fout,"w")
   sys.stdout = f_sal 
   #print(f"[JUNCTIONS]")
   for i in range(len(nudos)):
      print(f"{nudos[i][0]}  {nudos[i][1]}  {round(obtiene_demanda(dist_frec,float(nudos[i][2])),2)}  {nudos[i][3]}  ;")
   f_sal.close()
   sys.stdout = orig_stdout       
  

      
   
      