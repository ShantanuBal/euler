import datetime
start = datetime.datetime.now()

count = 0
for j in xrange(200,-1,-100): 
    for k in xrange(j,-1,-50):
        for l in xrange(k,-1,-20):
            for m in xrange(l,-1,-10):
                for n in xrange(m,-1,-5):
                    for o in xrange(n,-1,-2):
                        for p in xrange(o,-1,-1):
                            count += 1
                            print count

print datetime.datetime.now() - start
