import time, pdb, math
from fractions import *
start = time.time()

list = []
N = 1000000
for d in range(2,N+1):
    for n in range(1,d):
        f = Fraction(n,d)
        list.append(f)
list.sort()

for i in range(len(list)):
    if list[i] == Fraction(3,7):
        print list[i-1]
        break
print time.time() - start
