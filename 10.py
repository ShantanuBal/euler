import datetime
import math
start = datetime.datetime.now()

primes = [2,3]

each = 5
while primes[-1] < 100000:
    square_root = math.sqrt(each)
    for i in primes:
        if i <= square_root and each % i == 0:
            break
    else:
        primes.append(each)
    each += 2

print sum(primes) - primes[-1]

end = datetime.datetime.now()
print end - start
