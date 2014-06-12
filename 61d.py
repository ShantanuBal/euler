import time, pdb
start = time.time()

for i in xrange(11,100):
    for j in xrange(11,100):
        for k in xrange(11,100):
            for l in xrange(11,100):
                for m in xrange(11,100):
                    for n in xrange(11,100):
                        print i, j, k, l, m, n

print time.time() - start
