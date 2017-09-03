from PIL import Image,ImageDraw,ImageFont

import sys

import random



txt = '5'

im = Image.open('image.jpg')

ft = ImageFont.truetype("C:\\Windows\Fonts\STZHONGS.TTF",150)

draw = ImageDraw.Draw(im)



draw.text((480,0),txt,font=ft,fill='red')



im.show()