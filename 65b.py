import time, pdb, math
from fractions import *
start = time.time()

n = 4
period = [i if not (i-1)%3 else 1 for i in xrange(3,10-1)]
period = period[::-1]
period += [1,2,1]
print period

n,d = period[0], 1 
for each in period[1:]:
    flag=d; d=n; n=flag
    f1 = Fraction(n,d)
    f2 = Fraction(each,1)
    f = f1+f2
    n,d = f.numerator, f.denominator
f1 = Fraction(d,n)
f2 = Fraction(2,1)
f = f1+f2
n = f.numerator
print n

sum = 0
while n!=0:
    sum += n%10
    n /= 10
print sum

print time.time() - start
