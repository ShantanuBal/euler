import time
start = time.time()

def find_triplets(p):
    triplets = 0
    for i in xrange(1,p/2):
        for j in xrange(i+1,p/2):
            if i**2 + j**2 == (p-i-j)**2:
                triplets += 1
    return triplets

dict = {}
for i in xrange(5,1001):
   dict[i] = find_triplets(i)

max = 5
for i in xrange(6,1001):
    if dict[i] > dict[max]:
        max = i

print max
print time.time() - start
