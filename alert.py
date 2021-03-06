#! /usr/bin/python3
from apiCaller import rate


def currencyPosition(isLong,currency, initialPrice,sl):
    newPrice = rate(currency)


    if isLong:
        slPrice = initialPrice - sl
    else :
        slPrice = initialPrice + sl

    print ( str(round(newPrice,5)) + "," + str(round(slPrice,5)))
    
if __name__ == "__main__":
    currencyPosition(True,"AUDUSD",0.78133,0.03)

