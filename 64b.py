import time, math, pwd
start = time.time()

n = 1000
dict = {}
count = 0
for i in xrange(2,n+1):
    period = []
    rem = []
    a = math.sqrt(i)
    a0 = int(math.floor(a))
    a -= math.floor(a)    
    while a:
        a **= -1
        p, r = int(math.floor(a)), a%1.0
        if p == 2*a0: 
            period.append(p)
            dict[i] = len(period)
            if len(period) % 2 == 1:
                count += 1
            print i, a0, period
            break
        period.append(p)
        rem.append(r)
        a -= math.floor(a)

print count
print time.time() - start
