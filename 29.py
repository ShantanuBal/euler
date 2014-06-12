import datetime
start = datetime.datetime.now()

array = []
for i in xrange(2,101):
    new = []
    for j in xrange(2,101):
        new.append(pow(i,j))
    array.append(new)

big_array = []
for each in array:
    for number in each:
        big_array.append(number)
big_array.sort()
#print big_array

new_array = [big_array[0]]
for i in xrange(1,len(big_array)):
    if new_array[-1] == big_array[i]:
        continue
    new_array.append(big_array[i])
print len(new_array)

print datetime.datetime.now() - start
