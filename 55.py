import time
start = time.time()

count = 1

def palindrome(num):
    s = str(num)
    i = 0
    length = len(s)
    while i<length/2:
        if s[i] != s[length-1-i]:
            return 0
        i += 1
    return 1

def iterations(i):
    global count
    if count>50:
        return count
    j = i
    k = 0
    while i>0:
        k = k*10 + i%10
        i /= 10
    if palindrome(j+k):
        return count
    else: 
        count += 1
        return iterations(j+k)

n, iter = [],[]
for i in xrange(1,10000):
    x = iterations(i)
    n.append(i)
    iter.append(x)
    count = 1

for i in xrange(len(n)):
    print n[i]," -- ",iter[i]

ans = 0
for each in iter:
    if each>50:
        ans += 1
print ans

print time.time() - start
