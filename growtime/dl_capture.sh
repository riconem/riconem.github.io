#!/bin/bash

image_path=$1
login=$(cat dl_login)

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' --user $login -k http://10.255.255.1/)" != "200" ]]; do sleep 5; done

curl --user "$login" -k "http://10.255.255.1/dms?nowprofileid=1" >$image_path
