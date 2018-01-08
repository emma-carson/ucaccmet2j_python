#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

with open('precipitation.json') as my_file:
    precipitationdict = json.load(my_file)
    seattle_dict = [item for item in precipitationdict 
                     if item['station'] == 'GHCND:US1WAKG0038']

    sumseattle = sum(item['value'] for item in seattle_dict)
    
    monthlyRain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    month = [item['date'][5:7] for item in seattle_dict]
    
    value = [item['value'] for item in seattle_dict]
    
    monthvalue = zip(month,value)
    
    for k,v in monthvalue:
        monthlyRain[(int(k) - 1)] += v
    
    monthFractions = [x / sumseattle for x in monthlyRain]
    
    
    
    with open('results.json','w') as file:
        json.dump({"Seattle": {
                "totalYearlyPrecipitation" : sumseattle,
                "totalMonthlyPrecipitation" : monthlyRain,
                "state" : "WA",
                "relativeMonthlyPrecipitation": monthFractions,
                "Station" : "GHCND:US1WAKG0038"
            }
    },file)