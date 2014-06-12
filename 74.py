import time
start = time.time() 

N = 1000000
factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def fact_digits(x):
    sum = 0
    while x!= 0:
        digit = x % 10
        sum += factorial[digit]
        x /= 10
    return sum

dict = {}
ans = 0
for i in range(69,N):
    j = i
    array = [j]
    while True:
        j = fact_digits(j)
        if j in dict:
            dict[i] = len(array)+dict[j]
            if len(array)+dict[j] == 60:
                ans += 1
            break
        elif j in array:
            #print i,' ---> ',len(array)
            dict[i] = len(array)
            if len(array) == 60:
                ans += 1
            break

        else:
            array.append(j)

print ans
print time.time() - start
print len(dict)
