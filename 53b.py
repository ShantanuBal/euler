import time
start = time.time()

dict = {}
def factorial(n):
    i = n
    ans = 1
    while i>0:
        ans *= i
        i -= 1
    return ans

def combi(n,r):
    return (dict[n]/(dict[r]*dict[n-r]))

for i in xrange(0,101):
    dict[i] = factorial(i)

count = 0
for i in xrange(1,101):
    j = 0
    while j<=i:
        if combi(i,j) > 1000000:
            count += 1
            print count
        j += 1

print time.time() - start
