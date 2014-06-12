import time, math
start = time.time()

word = '1234567'
array = []

def swap(i,j):
    global word
    x,y = word[i], word[j]
    word = word.replace(x,'!')
    word = word.replace(y,x)
    word = word.replace('!',y)

def is_prime(x):
    if x%2 == 0:
        return 0
    for i in xrange(3,int(math.sqrt(x))+1,2):
        if x%i == 0:
            return 0
    return 1

def permute(i,n):
    global word, array
    if i==n:
        if is_prime(int(word)):
            array.append(int(word))
    else:
        for j in xrange(i,n+1):
            swap(i,j)
            permute(i+1,n)
            swap(i,j)

permute(0,len(word)-1)
print array


max = 0
for i in xrange(1,len(array)):
    if array[i] > array[max]:
        max = i
print array[max]

print time.time() - start
