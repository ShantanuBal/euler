from math import factorial

start_list = [str(i) for i in xrange(10)]
target = 1000000 - 1
target_list = ""

for i in xrange(9, -1, -1):
    f = factorial(i)
    target_list += start_list.pop(target / f)
    target %= f
    
print target_list
