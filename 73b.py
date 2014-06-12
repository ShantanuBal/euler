import time, pdb
start = time.time()
print "----------\nProblem 73\n----------"
N = 12000
primes, sieve = [], []
for i in range(N+1):
    sieve.append([])
for i in xrange(2,N+1):
    if not sieve[i]:
        primes.append(i)
        sieve[i] = 1
        j = 2*i
        while j<N+1:            
            sieve[j].append(i)
            j += i
#print sieve

count = 0
for i in xrange(2,N+1):
    if sieve[i] == 1:
        j = 1
        while float(j)/i < .5:
            if float(j)/i > float(1)/3:
                count += 1
                print j, i
            j += 1
    else:
        s = [0] * i 
        for each in sieve[i]:
            j = each
            while j<i:
                s[j] = 1
                j += each
        coprimes = [1]
        k = 2
        while k<i:
           if not s[k]:
                coprimes.append(k)
           k += 1
        j = 0
        while float(coprimes[j])/i < .5:
            if float(coprimes[j])/i > float(1)/3:
                count += 1
                print coprimes[j], i
            j += 1

print count       
print time.time() - start
