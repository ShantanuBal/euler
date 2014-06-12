import datetime
start = datetime.datetime.now()

import pdb

def divide(i):
    dict = {}
    remainder_string = []
    quotient = ""
    num = 10
    den = i
    while 1:
        #pdb.set_trace()
        if num < den:
            num *= 10
            quotient += "0"
            if len(remainder_string) > 0:
                remainder_string.append(remainder_string[-1])
            else: 
                remainder_string.append("0")
        else:
            char1 = num/den
            remainder = num%den
            quotient += str(char1)
            if remainder == 0:
                return 0
            
            num = remainder*10
            for i in xrange(len(quotient)-1):
                if quotient[i] == str(char1):
                    if remainder_string[i] == str(remainder):
                         return len(quotient)-1-i
            remainder_string.append(str(remainder))

max = 0
length = []
for i in xrange(2,1000):
    length.append(divide(i))
    if length[-1] > max:
        max = length[-1]
        pos = i
print max
print pos
print datetime.datetime.now()-start   
