import time, math
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
    while m!=1:
        if m % primes[i] == 0:
            m /= primes[i]
            n_primes.append(primes[i])
        else:
            i += 1

    array = [n_primes[0]]
    for each in n_primes[1:]:
        if each != array[-1]: 
            array.append(each)
    n_primes = array

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

def is_primes(i):
    if i % 6 not in [1,5]:
        return 0
    for j in xrange(2,int(math.sqrt(i))):
        if i%j == 0:
            return 0
    return 1

largest_n, largest_ans = 0, 0
for i in xrange(2,n+1):
    if is_primes(i):
        t_value = i-1
    else:
        t_value = find_t(i)
    ans = float(i)/float(t_value)
    print i, t_value, ans
    if ans > largest_ans:
        largest_ans, largest_n = ans, i

print largest_n
print time.time() - start
