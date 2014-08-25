import time
start = time.time()

primes = 1
m = 10000000
n = m/2
#check this
sieve = [0]*(n+1)
for i in xrange(1,(n/2)+1):
    den = ((n-i)/(2*i+1))+1
    for j in xrange(i,den):
        sieve[i+j+2*i*j] = 1

for i in xrange(1,n):
    if sieve[i] == 0:
        primes += 1

#print primes
print primes
print time.time() - start
