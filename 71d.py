import time, pdb, math
from fractions import *
start = time.time()

N = 1000
list = []
for i in range(1,N):
    for j in range(2*i,N+1):
        list.append(Fraction(i,j))
print time.time() - start
print "Sorting now"
list.sort()

#for each in list:
#    print each.numerator, "/", each.denominator, "   ",

for i in range(len(list)):
    if list[i] == Fraction(3,7):
        print "Answer: ", list[i-1]
        break
print time.time() - start
