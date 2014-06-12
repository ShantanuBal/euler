import datetime
start = datetime.datetime.now()

binary = '0b111111111111111111100000000000000000000'
number = int(binary, 2)
while number>0:
    number -= 1
    binary = bin(number)
    print binary

print datetime.datetime.now() - start
