function mul {
	local res=1
	for num in $@
	do
		let res=res*$num
	done
	echo "$res"

}


function isiteven {
	
	a=$(expr $1 % 2) 
	if [[ a -eq 0 ]] 
	then	return 0 
	else 
		return 1 
	fi
}



function nevens {

	local c=0
	for num in $@
	do
	local a=$(isiteven $num)
	if [[ $a -eq 0 ]]
	then 
	let c=c+1
	fi
	done
	echo "$c"

}



function howodd {

	local count=$(nevens $@)
	echo "$count"
}
