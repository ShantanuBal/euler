import time,pdb,math
start = time.time()

count = []
i = 1
n = 1
while i<100:
    if len(str(i)) > 1:
        break
    n = 1
    while n:
        digits = len(str(i**n))
        if digits == n:
            if i**n not in count:
                print i**n
                count.append(i**n)
        elif digits < n:
            break
        n += 1
    i += 1
    
print len(count)
print time.time() - start
