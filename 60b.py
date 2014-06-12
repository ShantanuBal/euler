import time
start = time.time()

n = 100000000
sieve = range(3,n,2)
top = len(sieve)
for each in sieve:
    if each:
        bottom = (each * each - 3) // 2
        if bottom >= top:
            break
        sieve[bottom::each] = [0] * -((bottom - top) // each)
primes = [2] + [each for each in sieve if each]
dict = {1:[]}
digits = 1
for each in primes:
    if len(str(each)) == digits + 1:
        digits += 1
        dict[digits] = [each]
    else:
        dict[digits].append(each)
print dict[8]

def check_combo(x):
    if int(str(3)+str(x)) in dict[len(str(x))+1] and int(str(x)+str(3)) in dict[len(str(x))+1] and int(str(7)+str(x)) in dict[len(str(x))+1] and int(str(x)+str(7)) in dict[len(str(x))+1] and int(str(109)+str(x)) in dict[len(str(x))+3] and int(str(x)+str(109)) in dict[len(str(x))+3] and int(str(673)+str(x)) in dict[len(str(x))+3] and int(str(x)+str(673)) in dict[len(str(x))+3]:
        return 1
    return 0

for a in xrange(len(dict[5])):
    print "3, 7, 109, 673, ", dict[5][a]
    if check_combo(dict[5][a]):
        print 792+dict[5][a]
        exit(0)
       
print time.time() - start
