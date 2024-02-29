#!/bin/bash

n=0
commmand=$1 #similiar to sys.argv[1] in py
while ! $command && [$n -l 5]; do
	sleep $n
	(n+=1)
	echo "Retry #$n"
done;
