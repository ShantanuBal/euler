import datetime
start = datetime.datetime.now()

count = 0
for i in xrange(0,201,1):
    for j in xrange(0,201,2):
        for k in xrange(0,201,5):
            for l in xrange(0,201,10):
                for m in xrange(0,201,20):
                    for n in xrange(0,201,50):
                        for o in xrange(0,201,100):
                            for p in xrange(0,201,200):
                                if i+j+k+l+m+n+o+p == 200:
                                    count += 1
                                    print count

print datetime.datetime.now() - start
