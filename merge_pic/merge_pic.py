#!/usr/bin/env python
# coding=utf-8
# Author = huhuhushan

import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def merge_pic(im1, im2):
    im1.thumbnail((393,1000))
    im2.thumbnail((393,1000)) # change the width of picture to 393.
    (x1, y1) = im1.size
    new_x = x1 * 2 + 14
    new_y = y1
    new_im = Image.new('RGB', (new_x, new_y), (255, 255, 255)) # create a white image
    new_im.paste(im1, (0, 0, x1, y1))
    new_im.paste(im2, (x1 + 14, 0, new_x, new_y))
    return new_im

def add_logo(im, logo):
    (new_x, new_y) = im.size
    (logo_x, logo_y) = logo.size
    new_im.paste(logo, (new_x - logo_x, new_y - logo_y, new_x, new_y),\
     mask=logo) # use mask to protect the transparent

    return new_im

if __name__ == '__main__':
    pre_name = 'wave'
    suf_name = '.png'
    pic_left = [1, 2, 3]
    pic_right = [4, 5, 6]
    for i in range(len(pic_left)):
        im1 = Image.open(pre_name+str(pic_left[i])+suf_name)
        im2 = Image.open(pre_name+str(pic_right[i])+suf_name)
        logo = Image.open('logo.png')
        new_im = merge_pic(im1, im2)
        new_im = add_logo(new_im, logo)
        new_im.show()
        name = pre_name + time.strftime('%m%d%H%M%S') + suf_name
        new_im.save(name)