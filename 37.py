import time
start = time.time()
import pdb

def no_even(x):
    x = str(x)
    for i in xrange(1,len(x)-1):
        if int(x[i]) in [2,4,6,8]:
            return 0
    return 1

n = 1000000
primes = [2]
sieve = [0] * n
for i in range(3,n,2):
    if sieve[i] == 0:
        if no_even(i):
            primes.append(i)
        j = i*2
        while j<n:
            sieve[j] = 1
            j += i

#print primes

def trunc(each):
    each = str(each)
    for i in xrange(1,len(each)):
        if int(each[i:]) not in primes or int(each[:-i]) not in primes:
            return 0
    return 1

trunc_primes = []
for each in primes:
    if trunc(each):
        trunc_primes.append(each)

print trunc_primes
print sum(trunc_primes[4:])
print time.time() - start
