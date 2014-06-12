import time
start = time.time()
x = 1000000

def sieveOfEratosthenes(n):
    sieve = range(3, n, 2)
    #print sieve
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

print len(sieveOfEratosthenes(x))
print time.time() - start
