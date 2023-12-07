#!/bin/bash

origin_path="/data/junlei/diffusion-pipeline/images/origin_imgs/"
generate_path="/data/junlei/diffusion-pipeline/images/new_img/images15/"
cd $generate_path;

for floder in `ls`
    do
        path=$generate_path$floder
        printf %s $path
        python -m pytorch_fid $origin_path $path
    done