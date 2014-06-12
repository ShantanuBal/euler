import time
start = time.time()

def is_palindrome(x):
    if str(x) != str(x)[::-1]:
            return 0
    return 1
    
def to_binary(x):
    bin = ''
    while x != 0:
        bin += str(x%2)
        x /= 2
    return bin[::-1]
 
palin_10, palin_2 = [],[]
for i in xrange(1,1000001,2):
    if is_palindrome(i):
        palin_10.append(i)

for each in palin_10:
    if is_palindrome(to_binary(each)):
        palin_2.append(each)

print sum(palin_2)
print time.time() - start
