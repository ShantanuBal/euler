import time, math
from fractions import gcd
start = time.time()

def gcde(x,y):
    while y != 0:
        flag = y
        y = x % y
        x = flag
    return x

count = 0
for i in xrange(2,12001):
    for j in xrange(int(math.ceil(float(i)/3)), int(math.floor(float(i)/2))):
        if gcd(i,j) == 1:
            count += 1
            print j, i
print count

print time.time() - start
