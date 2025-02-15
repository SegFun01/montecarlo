#!/bin/bash

echo "Iniciando Montecarlo"
echo "Generando series de valores aleatorios de caudal"

python3 generarCaudales.py

echo "Datos aleatorios generados..."
sleep 2

echo "Armando archivos de entrada a Epanet: *.INP"

for filename in junctions*.inp; do
    numero=${filename:9:3}
    salida=armado"${numero}".inp
    cat head.inp $filename bottom.inp > ${salida}
done
echo "Archivos de entrada listos..."

sleep 2

echo "Ejecutando Epanet con dada archivo de entrada"

for filename in armado*.inp; do
    numero=${filename:6:3}
    salida=armado"${numero}".rpt
    epanet2 $filename ${salida}
done

echo "Corridas de Epanet completadas"
sleep 2

echo "Extrayendo resultados de salidas de Epanet"
for filename in armado*.rpt; do
    numero=${filename:6:3}
    python3 leerRPT.py $filename
done
echo "Resultados extraídos"
sleep 2

echo "Unificando datos en un solo archivo: unido.csv" 
for filename in armado*.csv; do
    cat $filename >> unido.csv
done

echo "Resultados de Montecarlo están en unido.csv"
