#!/usr/bin/env python3
#_-*- coding:utf-8 -*-
# @Author: TAO
# @date: 2017-09-15

import requests
import json

url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101020100'
#url = r'http://api.caiyunapp.com/v2/YOUR_TOKEN/121.483,31.2333/forecast'
jsonStr = requests.get(url).text

data = json.loads(jsonStr)
weather = data["data"]

print("city:",weather["city"])
print("prompt:",weather["ganmao"])
for x in weather["forecast"]:
    print(x["date"],x["type"],x["high"],x["low"],x["fengxiang"],x["fengli"])
