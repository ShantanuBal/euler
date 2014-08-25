import time, math
start = time.time()

N = 100000
sieve = []
for i in xrange(N/2 + 1):
    sieve.append([])
for i in xrange(2,N/2):
    if sieve[i] == []:
        print i
        sieve[i] = 1
        j = i*2
        chain = [j - i]
        while j < N/2 + 1:
            sieve[j] += chain
            j += i
            chain.append(j - i)
print len(sieve)

print time.time() - start
