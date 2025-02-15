#!/bin/bash

for filename in armado*.csv; do
    cat $filename >> unido.csv
done

