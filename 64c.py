import time, math, pdb
start = time.time()

n = 13
dict = {}
count = 0
#pdb.set_trace()
for s in xrange(2,n+1):
    if math.sqrt(s) % 1 == 0:
        continue
    m, d, a = 0, 1, math.floor(math.sqrt(s))
    a0 = a
    period, array = 0,[]
    while True:
        m = d * a - m
        d = (s - m**2) / d
        a = math.floor( (a0+m)/d ) 
        array.append(a)
        period += 1
        if a == 2*a0:
            if period % 2 == 1:
                count += 1
            print s, a0, period, array
            break

print count
print time.time() - start
