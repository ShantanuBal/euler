import time, pdb, math
from fractions import *
start = time.time()

N = 1000000
primes = []
sieve = [0] * (N+1)
for i in xrange(2,N+1):
    if sieve[i] == 0:
        primes.append(i)
        sieve[i] = 1
        j = 2*i
        while j<N+1:            
            if sieve[j] == 0:
                sieve[j] = [i]
            else:
                sieve[j].append(i)
            j += i
print "Primes: ", len(primes)
#print "Sieve: ", sieve
"""
for i in xrange(4,N+1):
    if sieve[i] != 1:
        composite_sieve = [0]*i
        for factor in sieve[i]:
            j = factor
            while j<i:
                composite_sieve[j] = 1
                j += factor
        for k in xrange(1,i):
            list.append(Fraction(k,i))

list.sort()
for each in list:
    print each.numerator, "/",each.denominator,"   ",

for i in range(len(list)):
    if list[i] == Fraction(3,7):
        print list[i-1]
        break
"""
print time.time() - start
