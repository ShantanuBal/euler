import time
start = time.time()

n = 1000
sieve = [0] * n
primes = [2]
for i in xrange(3,n,2):
    if sieve[i] == 0:
        primes.append(i)
        j = i * 2
        while j < n:
            sieve[j] = 1
            j += i
print len(primes)

def check(number):
    factors = []
    i = 0
    while i<len(primes):
        if number%primes[i] == 0:
            factors.append(primes[i])
        i += 1
    return factors

i = 2
while i<200000:
    if len(check(i))==4 and len(check(i+1))==4 and len(check(i+2))==4 and len(check(i+3))==4:
        print i
        print i+1
        print i+2
        print i+3
        break
    i+= 1

print time.time() - start
