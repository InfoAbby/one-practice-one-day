from PIL import Image,ImageDraw,ImageFont
import sys
import random

def add_num(img):
    draw = ImageDraw.Draw(img)

    ft = ImageFont.truetype("C:\\Windows\Fonts\Arial.ttf",size=150)
    width,height=img.size
    draw.text((width-170,0),'99',font=ft,fill='red')

    img.show()


if __name__ == '__main__':
    img = Image.open('image.jpg')
    add_num(img)
    print('0')

