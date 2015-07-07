#!/bin/bash

set -e
set -u

if [ "$#" -ne 2 ]
then
  echo "Usage:"
  echo "  $0 people.txt start_port"
  echo "  $0 num_of_people start_port"
  exit 1
fi

if [ -f $1 ]
then
  people_file_base=$(basename $1)
  containers_file=containers_${people_file_base%.*}.txt
  names=$(sed -e 's/"\?\(.*\)@.*/\1/g' $1)
elif [ -n "$1" ] && [ -z "${1##[0-9]}" ]
then
  containers_file=containers_$(date +"%Y-%m-%d_%H-%M").txt
  names=$(seq -f "%.0f_of_$1" $1)
else
  echo "'$1' is not a file or integer"
  exit 1
fi

port=$2;

# create an empty file
> $containers_file

for NAME in $names
do
    user=$NAME
    password=$(pwgen -s -B 13 1)
    cont_name=python-grass-addon-${user}

    docker run -d -P \
        --name $cont_name \
        -p ${port}:8888 \
        -w /notebooks \
        -e "PASSWORD=${password}" \
        -e "PEM_FILE=/key.pem" \
        -e "USE_HTTP=0" \
        -e "GRASS_BATCH_JOB=/src/notebook.sh" \
        wenzeslaus/python-grass-addon \
        grass70 /grassdata/nc_basic_spm_grass7/user1 > /dev/null

    echo $cont_name >> $containers_file
    echo "${user} https://fatra.cnr.ncsu.edu:${port} ${password}"
    let port++
done
