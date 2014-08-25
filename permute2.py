import time, math
start = time.time()

word = "abcdefgh"
leng = 0

def swap(i,j):
    global word
    array = [each for each in word]
    flag = array[i]
    array[i] = array[j]
    array[j] = flag
    word = ""
    for each in array:
        word += each

def permute(k):
    for j in xrange(1, len(word)):
        swap(k%(j+1),j)
        k = k/(j+1)

for i in xrange(0,math.factorial(8)):
    word = "abcdefgh"
    permute(i)
    print word
    leng += 1

print leng
print time.time() - start
