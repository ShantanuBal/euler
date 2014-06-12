import time, pdb
start = time.time()

n = 100000000
sieve = [0]*n
primes = [2]
i = 3
while i<n:
    if sieve[i] == 0:
        primes.append(i)
        j = i*2
        while j<n:
            sieve[j] = 1
            j += i
    i += 2
print len(primes)

def j_in_primes(j):
    while primes[0]<j:
        primes.pop(0)
    if j==primes[0]:
        primes.pop(0)
        return 1
    return 0

count = 0
p = [3,5,7]
a = [1,2,3,4,5,6,7,8,9]
diag = [1,3,5,7,9]
i = 3
while 1:
    j = (i**2)+1
    i += 2
    while j<=i**2:
        a.append(j)
        if (j-1)%(i-1) == 0:
            diag.append(j)
            if j_in_primes(j):
                p.append(j)
        j += 1
    print float(len(p))/float(len(diag))," -- ",p[-1]," -- ",i
    if float(len(p))/float(len(diag))<.10:
        break
    count += 1
print len(primes)

print time.time() - start
