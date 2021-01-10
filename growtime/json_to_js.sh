#!/bin/bash

image_folder=$1
json_file=$(cat "images/$image_folder/images.json")
js_file_path=dist/images.js

js_end='.map( e => {return "images/'$image_folder'/" + e});'
js_data=''$json_file''$js_end''

sed -i "/$image_folder.*/c\var $image_folder = $js_data" $js_file_path
