#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import deepzoom

INPUT_DIR = '../img/maps'
OUTPUT_DIR = '../img/map_zooms'


CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def main(input_dir, output_dir, pattern):

    input_filenames = glob.glob(os.path.join(CUR_DIR, input_dir, pattern))

    creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="jpg",
                                    image_quality=0.7, resize_filter="bicubic")

    for filename in input_filenames:
        print(filename)
        basename = os.path.basename(filename).split('.')[0]

        output_file = os.path.join(CUR_DIR, output_dir, basename + ".dzi")
        creator.create(filename, output_file)


main(INPUT_DIR, OUTPUT_DIR, "hughes_1891.jpg")
# Specify your source image
#SOURCE = "helloworld.jpg"

# Create Deep Zoom Image creator with weird parameters

# Create Deep Zoom image pyramid from source
#creator.create(SOURCE, "helloworld.dzi")
