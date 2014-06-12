import datetime
import math
start = datetime.datetime.now()

def find_divisors(num):
    array = [1]
    for i in xrange(2, int(math.sqrt(num))+1):
        if num%i == 0:
            array.append(i)
            array.append(num/i)
    return array

abundant = []
for i in range(3, 28124):
    divisors = find_divisors(i)
    if sum(divisors) > i:
        abundant.append(i)
print "calculated all abundants"

list = []
for i in range(0, len(abundant)):
    for j in range(i, len(abundant)):
        list.append( abundant[i]+abundant[j])
print "calculated all possible sum of abundants"

list.sort()
print "sorting done in..."+str(datetime.datetime.now()-start)

new = []
position = 0
while list[position] < 28124:
    if list[position] == list[position+1]:
        position += 1
    else:
        new.append(list[position])
        position += 1
print sum(new)

print datetime.datetime.now()-start
