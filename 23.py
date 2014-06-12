import datetime
start = datetime.datetime.now()

def find_divisors(num):
    array = []
    p = 1
    q = num/p
    while p < q:
        if num % p == 0:
            array.append(p)
            q = num/p
            if q != p:
                array.append(q)
        p += 1
    return array

abundant = []
for i in range(3, 28124):
    divisors = find_divisors(i)
    if sum(divisors) > 2*i:
        abundant.append(i)
print "calculated all abundants till 28123"

list = []
for i in range(0, len(abundant)):
    for j in range(i, len(abundant)):
        list.append( abundant[i]+abundant[j])
print "calculated all possible sum of abundants"

list.sort()
print "sorting done..."

new = []
position = 0
while list[position] < 28124:
    if list[position] == list[position+1]:
        position += 1
    else:
        print list[position]
        new.append(list[position])
        position += 1
print sum(new)

print datetime.datetime.now()-start
