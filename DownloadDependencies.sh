#! /bin/bash

array=$(sed -n "{s/,//p}" File.json )
failed_cmds=()
x=0
for i in $array
do
	if pip install $i; then
				
		echo "$i installed successfully!!!"
	else
		failed_cmds[$x]="$i"
		x=$(expr $x + 1)
   		echo "$i has been failed to install."
	fi

done
echo "!----------------Failed---------------!"
echo "Below $x commands are failed to installed"
for j in "${failed_cmds[@]}"
do
	echo "$j"
done
