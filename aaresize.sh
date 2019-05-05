#!/bin/bash
DIR=/mnt/Niceseagate/Ph/aadropstuffpls/resize/
FILES="${DIR}*"
n=0

for f in $FILES
do
  newname=${f//[[:blank:]]/_}
  mv "$f" "$newname"
  convert $newname -resize 700 $newname
  n=n+1
done
