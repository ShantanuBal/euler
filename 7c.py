import datetime
start = datetime.datetime.now()

primes = [2]

each = 3
while len(primes)<10001:
    mod_primes = []
    i = 0
    while primes[i] < each / 2:
        mod_primes.append(primes[i])
        i += 1
    for i in mod_primes:
        if i > each / 2:
            primes.append(each)
            break
        if each % i == 0:
            break
    else:
        primes.append(each)
    each += 1   
print primes[-1]

end = datetime.datetime.now()
print end - start
