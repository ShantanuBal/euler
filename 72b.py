import time, pdb, math
from fractions import *
start = time.time()
print "----------\nProblem 72\n----------"
N = 1000000
primes = []
sieve = range(N+1)
sieve[1] = 0
for i in xrange(2,N+1):
    if i == sieve[i]:
        primes.append(i)
        sieve[i] = i-1
        j = 2*i
        while j<N+1:            
            sieve[j] = sieve[j] * (i-1) / i
            j += i
count = 0
for each in sieve:
    count += each
print count
print time.time() - start
