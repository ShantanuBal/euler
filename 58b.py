import time, pdb
start = time.time()

n = 100000000
sieve = [0]*n
primes = [2]
i = 3
while i<n:
    if sieve[i] == 0:
        print i
        primes.append(i)
        j = i*2
        while j<n:
            sieve[j] = 1
            j += i
    i += 2
print len(primes)

print time.time() - start
