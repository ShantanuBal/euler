import time
start = time.time()

n = 1000000
sieve = range(3,n,2)
top = len(sieve)
for each in sieve:
    if each:
        bottom = (each * each - 3) // 2
        if bottom >= top:
            break
        sieve[bottom::each] = [0] * -((bottom - top) // each)
primes = [2] + [each for each in sieve if each]
print time.time()-start

def is_prime(y):
    if y % 6 not in [1,5]:
        return 0
    for each in primes:
        if each < y**.5:
            if y % each == 0:
                return 0
        else:
            return 1

def check(array):
    x = array[-1]
    l1 = len(str(x))
    for each in array[:-1]:
        l2 = len(str(each))
        if is_prime(int(str(each)+str(x))) and is_prime(int(str(x)+str(each))):
            continue
        else:
            return 0
    return 1

nn = 1229
for i in xrange(nn):
    for j in xrange(i+1, nn):
        if check([primes[i],primes[j]]):
            print [primes[i],primes[j]]
            for k in xrange(j+1, nn):
                if check([primes[i],primes[j],primes[k]]):
                    print [primes[i],primes[j],primes[k]]
                    for l in xrange(k+1, nn):
                        if check([primes[i],primes[j],primes[k],primes[l]]):
                            print [primes[i],primes[j], primes[k], primes[l]]
                            for m in xrange(l+1, nn):
                                if check([primes[i],primes[j],primes[k],primes[l],primes[m]]):
                                    print [primes[i],primes[j], primes[k], primes[l],primes[m]]," -- ", primes[i]+primes[j]+primes[k]+primes[l]+primes[m]
                                    print time.time() - start
                                    exit(0)
       
print time.time() - start
