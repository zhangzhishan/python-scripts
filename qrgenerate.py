#!/usr/bin/env python
# coding=utf-8
# Author = huhuhushan

from qrcode import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

data = 'http://code4fun.me'
qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
qr.add_data(data)
qr.make()

im = qr.make_image()
draw = ImageDraw.Draw(im)
xsize, ysize = im.size
#font = ImageFont.truetype("arial.ttf", 15)
text = 'code.me'
print im.size
subim = Image.open('logo.jpg')
print subim.size
subim = subim.resize((200, 200))
#font = ImageFont.load_default()
#draw.text((0, 0), text, 255, font = font)
#draw.text((0, 0), text, (255, 255, 255))
print subim.size
im.paste(subim, (xsize/2-100, ysize/2-100, xsize/2+100, ysize/2+100))
im.resize((50, 50))
im.size
im.show()

im.save('test2.jpg')
