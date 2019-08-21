#!/usr/bin/env bash

while getopts p:t: option
do
        case "${option}"
                in
                p) PID=${OPTARG};;
                t) TIMEOUT=${OPTARG};;
        esac
done

echo "Time (sec), CPU Load (%), Memory (%), Process Name, PID" > cpu_memory_output.csv

top -b -d 1 -p $PID n $TIMEOUT | awk -v OFS="," '$1+0>0 {print $9,$10,$NF,$1; fflush() }' >> raw_output.txt

nl -s "," raw_output.txt >> cpu_memory_output.csv