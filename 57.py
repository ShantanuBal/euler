import time,pdb
from fractions import *
start = time.time()

array = []
i = 1
a,b = 5,2
while i!=1001:
    f1 = Fraction(a,b)
    f2 = Fraction(1,1)
    array.append(f1-f2)
    flag = b; b = a; a = flag
    f1 = Fraction(a,b)
    f2 = Fraction(2,1)
    new = f1+f2
    a = new.numerator
    b = new.denominator
    i += 1

count = 0
for each in array:
    string = str(each)
    i = 0
    while i<len(string):
        if string[i] == '/':
             if i>len(string)-i-1:
                 count += 1    
        i += 1
print count

print time.time() - start
