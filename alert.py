#! /usr/bin/python3
from apiCaller import rate
import sys
import re

def currencyPosition(isLong,currency, initialPrice,sl):
    newPrice = rate(currency)


    if isLong:
        slPrice = initialPrice - sl
    else :
        slPrice = initialPrice + sl

    print ( str(round(newPrice,5)) + "," + str(round(slPrice,5)))
    
if __name__ == "__main__":
   n = str( sys.argv[1])
   initial = float(sys.argv[2])
   sldiff= float(sys.argv[3])
   direction = str(sys.argv[4])
   if re.match("long", direction,re.IGNORECASE):
       direction = True
   else:
       directon = False

   currencyPosition(direction,n,initial,sldiff)



