import urllib.request
import re

filename = '0008.html'
body_re = re.compile(r'<body>[\s\S]*?</body>')

def serachBody(filename):
    with open(filename,'r') as f:
        data = f.read()
        body = body_re.findall(data)
    print(''.join(body))


if __name__ == '__main__':
    serachBody(filename)