import time

N = 10000000

start = time.time()
count = 0
while count<N:
    count += 1
print "While loop done...", count
print time.time() - start

start = time.time()
for count in xrange(N):
    continue
print "For loop done...", count
print time.time() - start
