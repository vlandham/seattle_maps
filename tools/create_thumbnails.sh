#!/bin/bash

input_dir="img/maps"
output_dir="img/thumb/"

mogrify -resize 400 -quality 85 -path $output_dir $input_dir/*.jpg
