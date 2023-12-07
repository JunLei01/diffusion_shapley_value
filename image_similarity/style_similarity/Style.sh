#!/bin/bash

origin_path="/data/junlei/diffusion-pipeline/images/origin_imgs/mona_lisa_resize.png"
generate_path="/data/junlei/diffusion-pipeline/images/new_img/images15/"
run_path="/data/junlei/project-code/pytorch-AdaIN"
cd $generate_path;

for floder in `ls`
    do
        path=$generate_path$floder
        cd $path
        for image_name in `ls`
            do
                image_path=$path/$image_name
            done
        printf %s $image_path
        cd $run_path
        CUDA_VISIBLE_DEVICES=0 python test.py --content $origin_path --style $image_path
    done