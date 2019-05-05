#!/usr/bin/python
from pyowm import OWM
import sys
owm = pyowm.OWM('d0d96ecbe3deb5967eea39a88b09b17b')
location = sys.argv[1]

obs = owm.weather_at_place(location)
w = obs.get_weather()
print('Weather for ' + location + ' at:')
print(w.get_reference_time(timeformat='iso'))
print('Currently ' + w.get_detailed_status())
print('Temps:')
print('  ' + str(w.get_temperature('celsius')))
print('Rain: ' + str(w.get_rain()))
print('Clouds: ' + str(w.get_clouds()))
print('Wind:')
print('  ' + str(w.get_wind()))
print('Humidity: ' + str(w.get_humidity()))
print('Pressure:')
print('  ' + str(w.get_pressure()))
print('Snow: ' + str(w.get_snow()))
print('Sunrise at:')
print('  ' + str(w.get_sunrise_time('iso')))
print('Sunset at:')
print('  ' + str(w.get_sunset_time('iso')))
