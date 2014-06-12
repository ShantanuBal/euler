from math import factorial

start_list = [str(i) for i in xrange(3)]
print 'start list: ',start_list
target = factorial(3)-1
print 'target',target
target_list = ""
print

for i in xrange(2, -1, -1):
    print "step: ",i
    f = factorial(i)
    target_list += start_list.pop(target / f)
    print 'target_list: ',target_list
    target %= f
    print 'target: ',target
    
print target_list
