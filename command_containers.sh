#!/bin/bash

set -e
set -u

if [ "$#" -ne 2 ]
then
  echo "Usage: $0 command file.txt"
  exit 1
fi

while read NAME
do
    docker $1 $NAME
done < $2
