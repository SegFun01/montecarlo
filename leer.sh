#!/bin/bash

for filename in armado*.rpt; do
    numero=${filename:6:3}
    python3 leerRPT.py $filename
done

