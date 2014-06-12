import datetime
start = datetime.datetime.now()

array1 = []
array2 = []

length = 0
number = 1
while number < 1000000:
    original = number
    length = 0
    array1.append(number)
    print number, 
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        length += 1
    number = original + 1
    array2.append(length+1)
    print length
    print

print array2.index(max(array2)) + 1
print datetime.datetime.now() - start
