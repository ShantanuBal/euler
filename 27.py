import datetime
start = datetime.datetime.now()

def generate(i,j,primes):
    for p in xrange(1,70):
        if pow(p,2)+i*p+j not in primes:
            return 0
    return 1

flag = [0] * 10000
for i in xrange(2,10000):
    if flag[i] == 0:
        j = 2*i
        while j < 10000:
             flag[j] = 1
             j += i
primes = []
for i in xrange(2,len(flag)):
    if flag[i] == 0:
        primes.append(i)
print len(primes)   

combi = {}
for j in primes[0:168]:
    for i in xrange(-999,1000):
        if generate(i,j,primes):
            if j in combi:
                combi[j].append(i)
            else:    
                combi[j] = [i]  
print combi

print datetime.datetime.now() - start
