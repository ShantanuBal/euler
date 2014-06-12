import time, math, pwd
start = time.time()

n = 10000
dict = {}
count = 0
for i in xrange(2,n+1):
    period = []
    rem = []
    a = math.sqrt(i)
    a -= math.floor(a)    
    while a:
        a **= -1
        p, r = int(math.floor(a)), a%1.0
        if period and period[0] == p and abs(rem[0] - r) < 0.000001:
            dict[i] = len(period)
            if len(period) % 2 == 1:
                count += 1
            print i, len(period)
            break
        period.append(p)
        rem.append(r)
        a -= math.floor(a)

print count
print time.time() - start
