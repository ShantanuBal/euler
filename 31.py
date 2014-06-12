import datetime
start = datetime.datetime.now()

n = 200
combi = []
count = 0
for i in xrange(0,n+1): 
    for j in xrange(0,n/2+1):
        if i + 2*j > n:
            break 
        for k in xrange(0,n/5+1): 
            if i + 2*j + 5*k > n:
                break
            for l in xrange(0,n/10+1): 
                if i + 2*j + 5*k + 10*l > n:
                    break
                for m in xrange(0,n/20+1): 
                    if i + 2*j + 5*k + 10*l + 20*m > n:
                        break
                    for o in xrange(0,n/50+1): 
                        if i + 2*j + 5*k + 10*l + 20*m + 50*o > n:
                            break
                        for p in xrange(0,n/100+1):
                            if i + 2*j + 5*k + 10*l + 20*m + 50*o + 100*p > n:
                                break
                            for q in xrange(0,n/200+1): 
                                if i + 2*j + 5*k + 10*l + 20*m + 50*o + 100*p + 200*q > n:
                                    break
                                elif i + 2*j + 5*k + 10*l + 20*m + 50*o + 100*p + 200*q == 200:
                                    combi.append([i,j,k,l,m,o,p,q])
                                    print combi[-1]
                                    #count += 1
                                    #print count

print len(combi)
print datetime.datetime.now() - start
