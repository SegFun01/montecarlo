#!/bin/bash

for filename in junctions*.inp; do
    numero=${filename:9:3}
    salida=armado"${numero}".inp
    cat head.inp $filename bottom.inp > ${salida}
done

