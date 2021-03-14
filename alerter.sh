
a=0
update () {
 
 
 while true;
  
   do 
    output=$((python3 alert.py $1 $2 $3 $4) 2>&1)
    slP=${output:7}
    currP=${output:0:6}
    diff=$(echo "$2-$slP" | bc)
   
    stmt=$(echo "$diff>0" | bc -l) 
    if [ $stmt -eq 1 ];
    then
     stmt2=$(echo "$currP>$2" | bc -l) 
     if [ $stmt2 -eq 1 ];
     then
      status=✅
     else
      status=❗
     fi
    else
     stmt3=$(echo "$currP>$2"|bc -l)
     if [ $stmt -eq 1 ];
     then
      status=❗
     else
      status=✅
     fi
    fi
    terminal-notifier -title $status -message $1$output;
    sleep 10;
 done

}

start(){
  echo -n "Currency?"
  read curr
  echo -n "initial Position"
  read initial
  echo -n "sl diff?"
  read sl_diff
  echo -n "true for long;false for short"
  read pos
  update $curr $initial $sl_diff  $pos &
  echo $! > pid.txt
}


leave(){
 p=$(cat pid.txt)
 kill -9 $p

}

