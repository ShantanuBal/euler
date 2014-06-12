import time, pdb, math
start = time.time()

n = 400000000
sieve = [0]*n
primes = [2]
div = 2
len = 0
i = 3
print "SIDE -- DIAGS -- LENGTH -- RATIO"
while i<n:
    if math.sqrt(i) % 1 == 0 and math.sqrt(i) % 2 == 1:
        div += 2
        side = math.sqrt(i)
        diags = side*2 - 1
        print side," -- ",diags," -- ",len," -- ",float(len)/float(diags)
        if float(diags)*.10 > float(len):
            print "FOUND --> ",primes[-1]
            break
    elif sieve[i] == 0:
        if (i-1) % div == 0:
            len += 1
        primes.append(i)
        j = i*2
        while j<n:
            sieve[j] = 1
            j += i
    i += 2
#print primes

print time.time() - start
