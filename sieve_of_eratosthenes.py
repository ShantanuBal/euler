import time, pdb
start = time.time()

n = 1000000
sieve = range(3,n,2)
length = len(sieve)

for each in sieve:
    if each:
        if each*3>=n:
            break
        sieve[(each/2)-1+each::each] = [0]*((length-(each/2))/each)
count = 0

primes = [2] + [each for each in sieve if each]
#print primes
print len(primes)
print time.time() - start
