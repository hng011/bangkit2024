#!/bin/bash

for x in $(grep "jane_" "../data/test.txt"); do
    echo "/home/student-03-d5e9b0904681/"$x >> "oldFiles.txt"
done
