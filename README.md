# montecarlo

### Objetivo
A partir de un archivo con los datos de las demandas en los nudos del modelo, se obtienen valores aleatorios de caudal para cada nodo de acuerdo con una distribución de probabilidades.

### Requisitos
* Se debe aportar la o las curvas de probabilidad de caudales unitarios de los nodos, de la forma:
```
c_prob = [(15,0.75),(20, 0.9),(30, 1),(20,1.1),(15,1.25)]
```
```
0.75 ███████████████
0.90 ████████████████████
1.00 ██████████████████████████████
1.10 ████████████████████
1.25 ███████████████

```
![Gráfica de la distribución de probabilidades de caudales en el nodo](probabilidades.png)

La curva de probabilidades debe ser agregada al archivo `generarCaudales.py`.  Consisten en pares ordenados de (probabilidad, valor).   Representan la probabilidad de que el caudal de demanda promedio de cada nudo tenga un valor al azar en la curva de distribución normal alrededor del valor medio de la distribución.

* Se debe preparar un archivo de texto plano llamado `entrada.inp` con la información de los caudales promedio de los nudos, con los datos de id, caudal y observaciones:
```
J-1338 0.067596008 LasCruces 
J-1339 0.007246682 LasCruces 
J-1358 0.130367961 LasCruces 
J-1359 0.006647753 LasCruces 
J-1359 0.005991122 LasCruces 
J-1360 0.147128134 LasCruces
```
* Con el archivo `entrada.inp` se corre el programa `generarCaudales.py` que da un número `n` de archivos de llamados `junctions###.inp` que es un fragmento del archivo `inp` de entrada para Epanet:
```
python3 generarCaudales.py
```
* Se debe tener preparado el archivo del modelo en formato `inp` el cual debe ser editado para obtener 3 partes: `head.inp` con las primeras líneas de código hasta después de la instrucción `[DEMANDS]`, la segunda parte es el archivo `entrada.inp` descrito anteriormente y otra parte llamada `bottom.inp` con la parte baja del archivo `inp` habiendo eliminado la información desde el inicio hasta la instrucción `[DEMANDS]` incluida, por ejemplo en la muestra hasta antes de `[EMITERS]`.

* Se construye cada archivo de entrada a Epanet con las 2 partes, `head.inp`, `junctions###.inp` y `bottom.inp`, para generar un archivo llamado `armado###.inp` para cada corrida, así:
```
cat head.inp junctions.inp bottom.inp > armado###.inp
```

* Ahora con cada archivo que se llama `armado###.inp` se corre el modelo de Epanet, y se obtienen archivos con nombre `armado###.rpt`, en donde `###` lo irá generando el scrit de bash, que corre `n` veces.
```
epanet2 armado###.inp armado###.rpt
```
**Nota:**  el comando anterior es para usar en Epanet para Linux.  En Windows usar `runepanet.exe` en lugar de `epanet2`.


Con la lista de archivos llamados  `armado000.rpt`, `armado001.rpt`, `armado002.rpt`, ... `armado999.rpt`, se prepara múltiples archivos en formato de CSV, que se llama `armado###.csv`, y también en formato json `armado###.json`.  
```
python3 leerRPT.py
```

## Script unificado
El SCRIPT `montecarlo.sh` realiza todo el proceso de generar los sets de caudales aleatorios para cada corrida, confeccionar cada uno de los `n` archivos INP de entrada para el EPANET, realizar las corridas, extraer los datos de cada corrida y unificar los resultados en un único archivo CSV, que se llama `unido.csv`.  

Nota:  en la etapa de pruebas  `montecarlo.sh` realiza un análisis con 10 corridas, sin embargo en la prueba final deberá hacerse con 1000 veces.  Esto se debe editar en `generarCaudales.py`, hay que editar `n=10`, por `n=1000`

crc2025
  
