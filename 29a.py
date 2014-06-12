import datetime

start = datetime.datetime.now()

l = []
for a in range(2,101):
        for b in range (2,101):
                c = a**b
                if c not in l:
                        l.append(c)
print len(l)

print datetime.datetime.now() - start
