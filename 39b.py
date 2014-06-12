import time, math
start = time.time()

triplets = {}
for i in xrange(1,1000):
    triplets[i] = 0

for i in xrange(1,500):
    for j in xrange(i+1,500):
        sol = math.sqrt(i**2 + j**2)
        if sol%1 == 0 and sol+i+j < 1000:
            triplets[int(sol+i+j)] += 1

max = 1
for i in xrange(2,1000):
    if triplets[i] > triplets[max]:
        max = i
print max

print time.time() - start
