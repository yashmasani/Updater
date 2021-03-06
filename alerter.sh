
a=0
update () {

 while true; 
   do 
    output=$((python3 alert.py) 2>&1)
    echo $output
    terminal-notifier -title '💰' -message $output;
    sleep 10;
 done

}

start(){
  update &
  echo $! > pid.txt
}


leave(){
 p=$(cat pid.txt)
 kill -9 $p

}

