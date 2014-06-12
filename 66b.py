import time, math
start = time.time()

def find(d):
    for i in xrange(2,100000000):
        if not math.sqrt((i**2 - 1)/float(d)) % 1:
            return [d,i]   
       
ans = []
for i in xrange(2,1000+1):
    if math.sqrt(i)%1:
        ans.append(find(i))
        print ans[-1]

largest,d = ans[0][1],ans[0][0]
for each in ans[1:]:
    if each[1] > largest:
        largest,d = each[1], each[0]
print d, largest

print time.time() - start
