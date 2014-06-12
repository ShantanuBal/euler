import time, pdb, math
start = time.time()

x = 500000000
def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

primes = sieveOfEratosthenes(x)
first = time.time()

print "SIDE -- DIAGS -- PRIMES -- RATIO"
count = 3
len = 1
for i in primes:
    if i > count**2:
        diags = count*2 - 1
        print count," -- ",diags," -- ",len-1," -- ",float(len-1)/float(diags)
        count += 2
        if float(diags)*.10 > float(len-1):
            print "FOUND --> ", count
            break
    if (i-1)%(count-1) == 0:
        len += 1

print first - start
print time.time() - first
