import time, pdb, math
from fractions import *
start = time.time()

N = 1000
primes = [2]
sieve = [0] * N

for i in xrange(3,N+1,2):
    if not sieve[i]:
        primes.append(i)
        j = i
        while j<N+1:            
            sieve[j] = 1
            j += 2*i

print len(primes)
print time.time() - start

list = []
for i in primes:
    for j in range(1,i/2+1):
        list.append(Fraction(j,i))
list.sort()
#print list

for i in range(len(list)):
    if list[i] == Fraction(3,7):
        print "Answer: ", list[i-1]
        break
print time.time() - start
