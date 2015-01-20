import urllib.request
import random

domain = 'http://ah.189.cn/sso/VImage.servlet?random='

for i in range(51, 100):
    a = random.random()
    url = domain + str(a)
    g = urllib.request.urlopen(url)
    with open('test' + str(i) + '.jpg', 'b+w') as f:
        f.write(g.read()) 
