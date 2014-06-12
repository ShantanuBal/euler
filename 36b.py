import time
start = time.time()

def is_palindrome(x):
    length = len(str(x))
    for i in xrange(length/2):
        if str(x)[i] != str(x)[length-1-i]:
            return 0
    return 1
    
def to_binary(x):
    return str(x)[::-1]
 
array = []
for i in xrange(1,1000001,2):
    if is_palindrome(i) and is_palindrome(to_binary(i)):
        array.append(i)

print sum(array)
print time.time() - start
