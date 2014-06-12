import datetime
start = datetime.datetime.now()

def sum_of_powers(i):
    sum = 0
    while i!=0:
        sum += (i%10)**5
        i /= 10
    return sum

i = 354294
sum = 0
while i>100:
    if i == sum_of_powers(i):
       sum += i 
    i -= 1

print sum
print datetime.datetime.now() - start
