import time, pdb
start = time.time()

prime_length = 2
seq = 6
n = 1000000
sieve = range(3,n,2)
top = len(sieve)
for each in sieve:
    if each:
        bottom = (each*each - 3)//2
        if bottom >= top:
            break
        sieve[bottom::each] = [0] * -((bottom-top) // each)
primes = [2] + [each for each in sieve if each]
dict = {}
count = 1
for each in primes:
    if len(str(each)) > count:
        count += 1
    if count in dict:
        dict[count].append(each)
    else:
        dict[count] = [each]
primes,primes2 = [],[]

def merge(code,pri):
    #pdb.set_trace()
    pos = []
    i = 0
    while i<len(code):
        if code[i] == '1':
            pos.append(i)
        i += 1

    # check if all are the same digit
    first = pri[pos[0]]
    for each in pos[1:]:
        if pri[each] != first:
            return 0

    # check if digit is less that sequence limit
    if int(pri[pos[0]]) > 10-seq:
        return 0

    # check incrementally
    pri2 = ''
    for i in xrange(0,len(pri)):
        if i in pos:
            pri2 += 'x'
        else:
            pri2 += pri[i]
    pri = pri2

    count = 1
    first = int(first)+1
    while seq-count <= 10-first:
        new_pri = ''
        for each in pri:
            if each == 'x': 
                new_pri += str(first)
            else:
                new_pri += each
        if int(new_pri) % 6 in [1,5] and int(new_pri) in primes2:
            count += 1
        first += 1

    if count == seq:
        print pri
        return 1
    return 0

def check(pri):
    i = 1
    length = len(str(pri))
    limit = 2**(length-1)
    while i < limit:
        code = bin(i)[2:]
        if merge('0'*(length-1-len(code))+code,str(pri)) == 1:
            return 1
        i += 1
    return 0

#pdb.set_trace()
while prime_length<7:
    primes = dict[prime_length]
    primes2 = primes[:]
    print primes2
    for each in primes:
        print each
        if check(each):
            #break
            print time.time() - start
            exit(0)
        else:
            primes2.remove(each)
    prime_length += 1
#print dict
print time.time() - start
