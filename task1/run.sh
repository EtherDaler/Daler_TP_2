#!/bin/bash

for opt in 1 2 3 4
do
    case $1 in
	--input_folder) folder=$2;;
        --extension) ext=$2;;
        --backup_folder) backup_f=$2;;
        --backup_archive_name) arch_name=$2;;
    esac
    shift 2
done




mkdir $backup_f

for file in $(find $folder -type f -name "*.$ext")
do
	cp --backup=numbered $file $backup_f
done

tar -czpf $arch_name $backup_f

echo 'done'
