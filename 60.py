import time
start = time.time()

n = 10000000
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
#print dict

def check_combo(a,b,c,d,e):
    array = [a,b,c,d,e]
    for i in xrange(len(array)-1):
        for j in xrange(i+1,len(array)):
            length = len(str(array[i])) + len(str(array[j]))
            x = int(str(array[i])+str(array[j]))
            y = int(str(array[j])+str(array[i]))
            if x % 6 in [1,5] and y % 6 in [1,5] and x in dict[length] and y in dict[length]:
                continue
            else: 
                return 0
    return 1

for a in xrange(len(dict[1])-1):
    for b in xrange(a+1, len(dict[1])):
        if int(str(dict[1][b])+str(dict[1][a])) in dict[2] and 
        for c in xrange(len(dict[3])-1):
            for d in xrange(c+1, len(dict[3])):
                for e in xrange(len(dict[4])):
                    print dict[1][a],dict[1][b],dict[3][c],dict[3][d],dict[4][e]
                    if check_combo(dict[1][a],dict[1][b],dict[3][c],dict[3][d],dict[4][e]):
                        print dict[1][a]+dict[1][b]+dict[3][c]+dict[3][d]+dict[4][e]
                        exit(0)
       
print time.time() - start
