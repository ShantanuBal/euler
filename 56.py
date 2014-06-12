import time, pdb
start = time.time()

d_sum = []
for i in xrange(1,100):
    for j in xrange(1,100):
        num = i**j
        sum = 0
        while num>0:
            sum += num%10
            num /= 10
        d_sum.append(sum)

"""
max = d_sum[0]
for i in xrange(1,len(d_sum)):
    if d_sum[i]>max:
        max = d_sum[i]
print max
"""
print max(d_sum)

print time.time() - start
