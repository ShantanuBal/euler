import time, pdb
from fractions import *
start = time.time()

D = 1000000
def prin(x,y):
    print x,"/",y

n, d = 2, 5
while True:
    a = Fraction(n+1,d)
    if a < Fraction(3,7):
        n, d = n+1, d
        #n,d = a.numerator, a.denominator
        prin(n,d)
        if d>=D:
            break
        continue

    b = Fraction(n+1,d+1)
    if b < Fraction(3,7):
        n, d = n+1, d+1
        #n,d = b.numerator, b.denominator
        prin(n,d)
        if d>=D:
            break
        continue

print time.time() - start
