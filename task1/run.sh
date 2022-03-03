#!/bin/bash

while [ -n $1 ]
do
    case $1 in
	--input_folder) folder=$2;;
        --extension) ext=$2;;
        --backup_folder) backup_f=$2;;
        --backup_archive_name) arch_name=$2;;
    esac
    shift
done




mkdir $backup_f

for file in $(find $folder -type f -name "*.$ext")
do
	cp --backup=numbered $file $backup_f
done

tar -czpf $arch_name $backup_f

echo 'done'
