import time
from fractions import *
start = time.time()

count = 3
for d in range(9,12001):
    print d
    for n in range(1,d):
        if float(1)/float(3) < float(n)/float(d) < 0.50:
            count += 1
print count
print time.time() - start
