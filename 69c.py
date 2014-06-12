import time,math
start = time.time()

n = 1000000

length = 1000000
primes = [2]
sieve = [0]*length
i = 3
while i<length:
    if sieve[i] == 0:
        primes.append(i)
        j = i
        while j<length:
            sieve[j] = 1
            j += i
    i += 2
print len(primes)
        
def find_t(n):
    n_primes = []
    m = n
    i = 0
    while m!=0:
        if m%primes[i] == 0:
            m /= primes[i]
            if n_primes[-1] != primes[i]: 
                n_primes.append(primes[i])
        else:
            i += 1

    sieve = [0]*n
    for i in n_primes:
        j = i
        while j<n:
            sieve[j] = 1
            j += i
    count = 1
    for each in sieve[2:]:
        if each == 0:
            count += 1
    return count

largest_n, largest_ans = 0, 0
for i in xrange(2,n+1):
    t_value = find_t(i)
    ans = float(i)/float(t_value)
    print i, t_value, ans
    if ans > largest_ans:
        largest_ans, largest_n = ans, i

print largest_n
print time.time() - start
