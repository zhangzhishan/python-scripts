import Image 
import cPickle as pickle

DBFILE = 'task.pk'
def distance(str1, str2):
    same = [0, 0]
    total = [0, 0]
    for i in xrange(len(str1)):
        if str1[i] != 0:
            total[0] += 1
            if str1[i] == str2[i]:
                same[0] += 1
        if str2[i] != 0:
            total[1] += 1
            if str1[i] == str2[i]:
                same[1] += 1
    try:
        return 1 - 1.0 * same[0] / total[0] * 1.0 * \
                same[1] / total[1] * 1.0
    except:
        return 1
im = Image.open('test57.jpg')
#greyim = im.convert('L')
#greyim.show()
(Width, Height) = im.size
print im.size
pix = im.load()
Threshold = 150   
for i in xrange(Width):
    print pix[i,1]
    for j in xrange(Height):
        if pix[i, j] > (150, 150, 150): 
            pix[i, j] = (256, 256, 256)
        else:
            pix[i, j] = (0, 0, 0)
#im.show()
cropwidth = 12
pixsum = []
for i in xrange(Width):
    sum = 0
    for j in xrange(Height):
        if pix[i,j] == (0, 0, 0) :
            sum += 1
    pixsum.append(sum)
#print pixsum
block = []
for i in xrange(4):
    box = (0 + 15 * i, 0, 15 + 15 * i,20)
    im1 = im.crop(box)
    block.append(im1)
    #im1.show()
print block[1]
dist=[]
for k in xrange(4):
    for i in xrange(15):
        for j in xrange(20):
            if pix[i, j] == (0, 0, 0):
                dist.append(1)
            else:
                dist.append(0)

print dist[0:300]
try:
    samples = pickle.load(open(DBFILE, 'rb'))
except:
    samples = {}
    pickle.dump(samples, open(DBFILE, 'wb'))

ans = raw_input()
key=''
print dist[0:300]
for i in dist[0:300]:
    key += str(i)
samples[key] = ans
pickle.dump(samples, open(DBFILE, 'wb'))
            
pks = pickle.load(open(DBFILE, 'rb'))
samples = {}
r = []
for (pk, v) in pks.items():
    r.append(pk)
    samples[pk] = v
    print distance(pk, r[0]), v


