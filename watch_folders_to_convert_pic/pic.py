#!/usr/bin/env python
# coding=utf-8
# Author = huhuhushan

from PIL import Image

def large(im):
    (x, y) = im.size
    new_x = 640
    new_y = 480
    new_im = Image.new('RGB', (new_x, new_y), (255, 255, 255))
    rate_x = 1.0 * x / new_x
    rate_y = 1.0 * y / new_y
    rate = 1
    # Calculate the thumbnail rate, use the larger rate to fill the small part with blank
    if not (rate_x < 1 and rate_y < 1):
        if rate_x > rate_y:
            rate = rate_x
        else:
            rate = rate_y
    else:
        rate = rate_x if rate_x > rate_y else rate_y
    im.thumbnail((int(x / rate), int(y / rate)))
    (thumb_x, thumb_y) = im.size
    new_im.paste(im, ((new_x - thumb_x)/2, (new_y - thumb_y)/2, (new_x + thumb_x)/2, (new_y + thumb_y)/2))
    return new_im

def small(im):
    (x, y) = im.size
    new_x = 80
    new_y = 80
    new_im = Image.new('RGBA', (80, 80), (255, 255, 255))
    rate_x = 1.0 * x / new_x
    rate_y = 1.0 * y / new_y
    rate = 1
    # Calculate the thumbnail rate
    # use the smaller rate and crop the pic in the center
    rate = rate_x if rate_x < rate_y else rate_y
    im.thumbnail((int(x / rate), int(y / rate)), Image.ANTIALIAS)
    (thumb_x, thumb_y) = im.size
    new_im.paste(im, ((new_x - thumb_x)/2, (new_y - thumb_y)/2, (new_x + thumb_x)/2, (new_y + thumb_y)/2))
    return new_im

if __name__ == '__main__':

    im = Image.open('./1.png')
    new_im = large(im)
    new_im.save('large.jpg')
    new_im = small(im)
    new_im.show()
    new_im.save('./small.png', quality = 95)
