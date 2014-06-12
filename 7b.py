import datetime
start = datetime.datetime.now()

primes = [2]

each = 3
while len(primes)<10001:
    i = 0
    while i < len(primes) and primes[i] < each: 
        if each % primes[i] == 0:
            break
        i += 1
    else:
        primes.append(each)
    each += 1   
print primes[-1]

end = datetime.datetime.now()
print end - start
