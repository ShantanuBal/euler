import math, datetime

start = datetime.datetime.now()
def remainder_1to20(each):
    for i in range(2,20):
        if each % i != 0:
            return 0
        if ( each / i ) % 2 != 0:
            return 0
    return 1

# compute primes
primes = []
each = 21
while each > 20:
    x = remainder_1to20(each)
    if x == 1:
        break
    each += 1
print "answer --> ", each
end = datetime.datetime.now()
print end - start
