import time
start = time.time()

factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def sum_of_factorial(x):
    sum = 0
    for each in str(x):
        sum += factorial[int(each)]
    return sum

i = 10
count = 0
real_sum = 0
while i < 362880*9:
    if sum_of_factorial(i) == i:
        real_sum += i
        count += 1
        print i
    i += 1

print time.time() - start
