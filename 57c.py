import time
start = time.time()
def p57():
    i = 0 # iteration
    n = 1 # numerator
    d = 1 # denominator
    count = 0
    while i <= 1000:
        dd = d + n   # next denominator
        nn = d + dd  # next numerator
        n,d = nn,dd
        i += 1
        if len(str(n)) > len(str(d)):
            count += 1
    return count

print p57()
print time.time() - start
