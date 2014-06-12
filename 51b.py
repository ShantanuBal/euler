import time, pdb
start = time.time()

x = 1000000

def sieve(n):
    sieve = range(3,n,2)
    top = len(sieve)
    for each in sieve:
        if each:
            bottom = (each*each - 3)//2
            if bottom >= top:
                break
            sieve[bottom::each] = [0] * -((bottom-top) // each)
    return [2] + [each for each in sieve if each]

print len(sieve(x))
print time.time() - start
