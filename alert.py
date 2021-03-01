#! /usr/bin/python3
from apiCaller import rate


def currencyPosition(isLong,currency, initialPrice,sl):
    newPrice = rate(currency)


    if isLong:
        slPrice = initialPrice - sl
    else :
        slPrice = initialPrice + sl

    
    return round(newPrice-initialPrice,5), round(slPrice,5)
    

