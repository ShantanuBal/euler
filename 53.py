import time
start = time.time()

def factorial(n):
    i = n
    ans = 1
    while i>0:
        ans *= i
        i -= 1
    return ans

def combi(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

count = 0
for i in xrange(1,101):
    j = 0
    while j<=i:
        if combi(i,j) > 1000000:
            count += 1
            print count
        j += 1

print time.time() - start
