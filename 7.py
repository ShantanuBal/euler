import datetime
start = datetime.datetime.now()

primes = []

each = 2
while len(primes)<10001:
    for i in range(2,each/2+1):
        if each % i == 0:
            break
    else:
        primes.append(each)
    each += 1   
print primes[-1]

end = datetime.datetime.now()
print end - start
