#!/bin/bash

echo "Nombre de la corrida: "
read nombre

for filename in armado*.rpt; do
    numero=${filename:6:3}
    salida="${nombre}"-"${numero}".rpt
    mv $filename ${salida}
done

echo "Archivos rpt renombrados..."

sleep 2

for filename in armado*.json; do
    numero=${filename:6:3}
    salida="${nombre}"-"${numero}".json
    mv $filename ${salida}
done

echo "Archivos json renombrados"
sleep 2

echo "Fin del proceso de renombrar corrida..."
