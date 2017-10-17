import urllib.request
import re

filename = '0008.html'
body_re = re.compile(r'"((https|ftps|http|ftp)://.*?)"')
def serachBody(filename):
    with open(filename,'r') as f:
        data = f.read()
        body = body_re.findall(data)
    print(body)


if __name__ == '__main__':
    serachBody(filename)