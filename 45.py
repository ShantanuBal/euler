import time, math
start = time.time()

pent = []
hex = []

for i in xrange(1,100000):
    pent.append(i*(3*i-1)/2)

for each in pent:
    if ((1+math.sqrt(1+8*each))/4) % 1 == 0:
        print each

print time.time() - start
