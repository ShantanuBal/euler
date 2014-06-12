import time
start = time.time()
print "--------------------------\nProblem 72\n--------------------------"

def sieve(n):
    sieve = range(3,n,2)
    for i in xrange(len(sieve)):
        if sieve[i]:
            sieve[i+sieve[i]::sieve[i]] = [0] * (((n/2 - 2 -i) / sieve[i]))
    return [2] + [each for each in sieve if each]

N = 1000000
primes = sieve(N)
print len(primes)

count = 0
for each in primes:
    count += (each - 1)

print time.time() - start
