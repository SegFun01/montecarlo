#!/bin/bash

for filename in armado*.inp; do
    numero=${filename:6:3}
    salida=armado"${numero}".rpt
    epanet2 $filename ${salida}
done

