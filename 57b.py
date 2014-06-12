import time,pdb
from fractions import *
start = time.time()

array = []
i = 1
a,b = 5,2
count = 0
while i!=1001:
    f1 = Fraction(a,b); f2 = Fraction(1,1)
    f = f1-f2
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1
    #array.append(f1-f2)
    flag = b; b = a; a = flag
    f1 = Fraction(a,b)
    f2 = Fraction(2,1)
    new = f1+f2
    a = new.numerator
    b = new.denominator
    i += 1

print count

print time.time() - start
