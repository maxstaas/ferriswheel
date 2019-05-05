#!/usr/bin/python
import pyowm
import sys
owm = pyowm.OWM('d0d96ecbe3deb5967eea39a88b09b17b')
location = sys.argv[1]

fc = owm.three_hours_forecast(location)
f = fc.get_forecast()
x=2
for weather in f:
  if x==2:
    print(weather.get_reference_time('iso'),weather.get_status())
    x=0
  else:
    x+=1
