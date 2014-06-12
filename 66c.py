import time, math, pdb
start = time.time()

n = 1000
dict = {}
for s in xrange(2,n+1):
    if math.sqrt(s) % 1 == 0:
        continue
    m, d, a = 0, 1, math.floor(math.sqrt(s))
    a0 = int(a)
    array = []
    while True:
        m = d * a - m
        d = (s - m**2) / d
        a = math.floor( (a0+m)/d ) 
        array.append(int(a))
        if a == 2*a0:
            dict[s] = [a0,array]
            break

largest_d, largest_x = 0,0
for each in dict:
    #print each, dict[each]
    n, d, seq, i = [1,dict[each][0]], [0,1], dict[each][1], 0
    while True:
        if not n[-1]**2 - each * d[-1]**2 - 1:
            print n[-1], each, d[-1]
            if n[-1] > largest_x:
                largest_x, largest_d = n[-1], each
            break
        n.append(n[-1]*seq[i]+n[-2]); d.append(d[-1]*seq[i]+d[-2])
        if i == len(seq) - 1:
            i = 0
        else:
            i += 1

print largest_x, largest_d
print time.time() - start
