import time
start = time.time()
import pdb

primes = []
def all_combi(number):
    array = [number]
    i = 0
    number = str(number)
    while i < len(number) - 1:
        number += number[0]
        number = number[1:]
        array.append(int(number))
        if int(number) not in primes:
            return 0
        i += 1
    if len(array) > 1:
        for each in array:
            primes.remove(each)
    return array

n = 100
sieve = [0] * n
for i in xrange(2,n):
    if sieve[i] == 0:
        primes.append(i)
        j = i*2
        while j<n:
            sieve[j] = 1
            j += i
print len(primes)

new_primes = [2]
for each in primes:
    for digit in str(each):
        if int(digit) % 2 == 0:
            break
    else:
        new_primes.append(each)
primes = new_primes

circular_primes = []
for each in primes:
    #print each
    check = all_combi(each)
    if check:
        for every in check:
            circular_primes.append(each)

print circular_primes
print len(circular_primes)
print time.time() - start
