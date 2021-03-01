#! /usr/bin/python3

from urllib3 import PoolManager
import json


apiKey = "aa35584ed999d3f90445bcd054552998" 

url = "http://data.fixer.io/api/"


def rate(curr):
    
    endpoint = url +  "latest" + "?access_key=" + apiKey
    baseCurr = curr[3:]
    targetCurr = curr[:3]
    
    http = PoolManager()
    req = http.request("GET", endpoint)

    data = json.loads(req.data)
    base = data["rates"][baseCurr]
   
    exchangeRate=base

    if targetCurr != "EUR":
        # 1/targetcurr in schema
        target = data["rates"][targetCurr]

        exchangeRate= (1/target) * base
        # multiply with base curr in schema
    
    #care for bad apicall
    if req.status != 200:
        exchangeRate = 0
    return exchangeRate
