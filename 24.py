import datetime
start = datetime.datetime.now()

a = [0,1,2,3,4,5,6,7,8,9]
b = [0,1,2,3,4,5,6,7,8,9]
c = [0,1,2,3,4,5,6,7,8,9]
d = [0,1,2,3,4,5,6,7,8,9]
e = [0,1,2,3,4,5,6,7,8,9]
f = [0,1,2,3,4,5,6,7,8,9]
g = [0,1,2,3,4,5,6,7,8,9]
x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
z = [0,1,2,3,4,5,6,7,8,9]

list = []
for i in xrange(0, len(a)):
    for j in xrange(0, len(b)): 
        if j == i:
            continue
        for k in xrange(0, len(c)):
            if k in [i,j]:
                continue
            for l in xrange(0, len(d)):
                if l in [i,j,k]:
                    continue
                for m in xrange(0, len(e)):
                    if m in [i,j,k,l]:
                        continue
                    for n in xrange(0, len(f)):
                        if n in [i,j,k,l,m]:
                            continue
                        for o in xrange(0,len(g)):
                            if o in [i,j,k,l,m,n]:
                                continue
                            for p in xrange(0, len(x)):
                                if p in [i,j,k,l,m,n,o]:
                                    continue
                                for q in xrange(0, len(y)):
                                    if q in [i,j,k,l,m,n,o,p]:
                                        continue
                                    for r in xrange(0, len(z)):
                                        if r in [i,j,k,l,m,n,o,p,q]:
                                            continue
                                        list.append( [a[i], b[j], c[k], d[l], e[m], f[n], g[o], x[p], y[q], z[r]] )
                                        if len(list) == 1000000:
                                            print list[-1]

word = ""
for each in list[999999]:
    word += str(each)
print word

print datetime.datetime.now()-start            
