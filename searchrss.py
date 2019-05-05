#!/usr/bin/python2
import feedparser
import sys

search = sys.argv[1]
rssfeed = 'https://nyaa.si/?page=rss&q=' + search + '&c=1_2&f=0'
d = feedparser.parse(rssfeed)
n=0
for entry in d.entries:
 date1 = entry.published_parsed
 date = str(date1.tm_year) + '-' + str(date1.tm_mon) + '-' + str(date1.tm_mday)
 name =  date + ' | ' + entry.nyaa_size + ' | ' + entry.nyaa_seeders + ' | ' + entry.nyaa_downloads + ' | ' + entry.title
 name = name.encode('ascii', 'ignore').decode('ascii')
 print (name)
 print (entry.link)
 n+=1
