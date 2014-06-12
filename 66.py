import time, math
start = time.time()

def find(d):
    for i in xrange(2,5000):
        for j in xrange(1,i):
            if not i**2 - d * j**2 - 1:
                return [d,i,j]   
       
ans = []
for i in xrange(2,1001):
    if math.sqrt(i)%1:
        ans.append(find(i))
        print ans[-1]

largest,d = ans[0][1],ans[0][0]
for each in ans[1:]:
    if each[1] > largest:
        largest,d = each[1], each[0]
print largest, d

print time.time() - start
