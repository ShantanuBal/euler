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
            j = i+1
            new_number = number/primes[i]
            while j<len(primes):
                if new_number%primes[j] == 0:
                    k = j+1
                    new_new_number = new_number/primes[j]
                    while k<len(primes):
                        if new_new_number%primes[k] == 0:
                            l = k+1
                            new_new_new_number = new_new_number/primes[k]
                            while l<len(primes):
                                if new_new_new_number%primes[l] == 0:
                                    return [primes[i],primes[j],primes[k],primes[l]]
                                l += 1
                        k += 1
                j += 1
        i += 1
    return 0

for i in xrange(2,200000):
    w,x,y,z = check(i),check(i+1),check(i+2),check(i+3)
    if w and x and y and z:
        print i,'--',w
        print i+1,'--',x
        print i+2,'--',y
        print i+3,'--',z
        break

print time.time() - start
