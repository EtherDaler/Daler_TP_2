#!/bin/bash
dirpath = $1
extension = $2
foldname = $3
archname = $4
mkdir $foldname
cp -r $dirpath $foldname
for i in $(find $foldname -type f -not -name "*.$extension")
do
	rm $i
done
for j in $(find $foldname -type d -empty)
do
	rm -d $j
done
tar -czpf $archname $foldname
echo done



