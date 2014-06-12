import datetime
start = datetime.datetime.now()

primes = [2,3]

each = 5
while primes[-1] < 2000000:
    for i in primes:
        if each % i == 0:
            break
    else:
        primes.append(each)
    each += 2

print sum(primes) - primes[-1]

end = datetime.datetime.now()
print end - start
