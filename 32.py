import time
start = time.time()
import pdb

def pandigital(a,b):
    #if a==39 and b==186:
    #    pdb.set_trace()
    pan_array = []
    for each in str(a):
        pan_array.append(each)
    for each in str(b):
        pan_array.append(each)
    for each in str(a*b):
        pan_array.append(each)
    for i in range(1,10):
        if str(i) not in pan_array:
            return 0
    return 1

list = []
for a in xrange(10,100):
    for b in xrange(100,1000):
        if len(str(a*b))==4 and pandigital(a,b):
            list.append(a*b)

for a in xrange(1,10):
    for b in xrange(1000,10000):
        if len(str(a*b))==4 and pandigital(a,b):
            list.append(a*b)
list.sort()
print list


new_list = [list[0]]
for each in list[1:]:
    if each != new_list[-1]:
        new_list.append(each)


print sum(new_list)
print time.time() - start
