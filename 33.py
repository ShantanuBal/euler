import time
start = time.time()

def is_curious(i,j):
    a,b = str(i), str(j)
    fraction = float(i)/float(j)
    if a[1] == '0' or b[1] == '0': 
        return 0
    elif a[0] not in b and a[1] not in b:
        return 0
    elif a[0] == b[0] and fraction == float(a[1])/float(b[1]):
        return 1
    elif a[0] == b[1] and fraction == float(a[1])/float(b[0]):
        return 1
    elif a[1] == b[0] and fraction == float(a[0])/float(b[1]):
        return 1
    elif a[1] == b[1] and fraction == float(a[0])/float(b[0]):
        return 1

curious = []
for i in xrange(11,100):
    for j in xrange(11,100):
        if i<j and is_curious(i,j):
            curious.append([i,j])

num,dec = 1,1
for each in curious:
    num *= each[0]
    dec *= each[1]

print num,"/",dec
print time.time() - start
