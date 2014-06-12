import time
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
        
def find_t(x):
    x_primes = []
    for each in primes:
        if each>x:
            break
        if x%each == 0:
            x_primes.append(each)
    count = 1
    for i in xrange(2,x): 
        if x%i == 0:
            continue
        for each in x_primes:
            if i%each == 0:
                break
        else:
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
