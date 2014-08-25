import time, math
start = time.time()

word = 'abcdefgh'
array = []
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

def permute(i,n):
    global word, array, leng
    if i==n:
        print word
        leng += 1
    else:
        for j in xrange(i,n+1):
            swap(i,j)
            permute(i+1,n)
            swap(i,j)

permute(0,len(word)-1)
print leng
print time.time() - start
