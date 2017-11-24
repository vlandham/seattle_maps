#!/bin/bash

input_dir="img/maps"
output_dir="img/thumb/"
pattern="rand_mcnally_1924.jpg"

mogrify -resize 400 -quality 85 -path $output_dir $input_dir/$pattern
