#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

url='http://horriblesubs.info/release-schedule/'

r = requests.get(url)
r.content

soup = BeautifulSoup(r.content,'html.parser')
#times = []
yespls = soup.find_all('td','schedule-show')
for a in yespls:
  a['class'] = 'schedule-page-show'

mon = soup.find('table','schedule-today-table')
animesmon = mon.find_all('td','schedule-page-show')
timesmon = mon.find_all('td','schedule-time')

tue = mon.find_next('table','schedule-today-table')
animestue = tue.find_all('td','schedule-page-show')
timestue = tue.find_all('td','schedule-time')

wed = tue.find_next('table','schedule-today-table')
animeswed = wed.find_all('td','schedule-page-show')
timeswed = wed.find_all('td','schedule-time')

thu = wed.find_next('table','schedule-today-table')
animesthu = thu.find_all('td','schedule-page-show')
timesthu = thu.find_all('td','schedule-time')

fri = thu.find_next('table','schedule-today-table')
animesfri = fri.find_all('td','schedule-page-show')
timesfri = fri.find_all('td','schedule-time')

sat = fri.find_next('table','schedule-today-table')
animessat = sat.find_all('td','schedule-page-show')
timessat = sat.find_all('td','schedule-time')

sun = sat.find_next('table','schedule-today-table')
animessun = sun.find_all('td','schedule-page-show')
timessun = sun.find_all('td','schedule-time')

#tob = sun.find_next('table','schedule-today-table')
#animestob = tob.find_all('td','schedule-page-show')

monrel=[]
tuerel=[]
wedrel=[]
thurel=[]
frirel=[]
satrel=[]
sunrel=[]
#tobrel=[]

def org_animes(a,t,c):
  x=0
  z=0
  for anime in a:
    anime = str(anime)
    if '</a>' in anime:
      anime = anime[:anime.find('</a>')]
    else:
      anime = anime[:anime.find('</td>')]
    anime = anime[anime.rfind('show\">')+6:]
    if t!=0:
      time = str(t[x])
      x+=1
      time = time[:time.find('</td>')]
      time = time[time.rfind('time\">')+6:]
      hour = int(time[:time.find(':')])+9
      if hour>=24:
        hour-=24
        z=1
      if hour<10:
        hour = '0'+str(hour)
      else:
        hour = str(hour)
      minute = time[time.find(':'):]
      time = hour+minute
      if z==1:
        c+=1
      if c==1: monrel.append(time + '\t' + anime)
      elif c==2: tuerel.append(time + '\t' + anime)
      elif c==3: wedrel.append(time + '\t' + anime)
      elif c==4: thurel.append(time + '\t' + anime)
      elif c==5: frirel.append(time + '\t' + anime)
      elif c==6: satrel.append(time + '\t' + anime)
      elif c==7: sunrel.append(time + '\t' + anime)
      elif c==8: monrel.append(time + '\t' + anime)
      if z==1:
        c-=1
    else:
      tobrel.append('\t' + anime)
  x+=1

def printanimes(a):
  for anime in a:
    print(anime)


org_animes(animesmon,timesmon,1)
org_animes(animestue,timestue,2)
org_animes(animeswed,timeswed,3)
org_animes(animesthu,timesthu,4)
org_animes(animesfri,timesfri,5)
org_animes(animessat,timessat,6)
org_animes(animessun,timessun,7)
#org_animes(animestob,0,0)

print('|Monday')
printanimes(monrel)
print('|Tuesday')
printanimes(tuerel)
print('|Wednesday')
printanimes(wedrel)
print('|Thursday')
printanimes(thurel)
print('|Friday')
printanimes(frirel)
print('|Saturday')
printanimes(satrel)
print('|Sunday')
printanimes(sunrel)
#print('|To be scheduled')
#printanimes(tobrel)
