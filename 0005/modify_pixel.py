from PIL import Image
import glob,os

size = 1136,640

def thumbnail_pic():
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        print(file,ext)
        im = Image.open(infile)
        im.thumbnail(size)
        print(im.format, im.size, im.mode)
        im.save(file +".thum.jpeg")

if __name__ == '__main__':
    path = '.'
    thumbnail_pic()