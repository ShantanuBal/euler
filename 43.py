import time, math
start = time.time()

word = '123'
array = []

def swap(i,j):
    global word
    x,y = word[i], word[j]
    word = word.replace(x,'!')
    word = word.replace(y,x)
    word = word.replace('!',y)

def holds_property(x):
    if len(x) == 10 and int(word[1:4]) % 2 == 0 and int(word[2:5]) % 3 == 0 and int(word[3:6]) % 5 == 0 and int(word[4:7]) % 7 == 0 and int(word[5:8]) % 11 == 0 and int(word[6:9]) % 13 == 0 and int(word[7:10]) % 17 == 0:
        return 1
    return 0

def permute(i,n):
    global word, array
    if i==n:
        print word
        array.append(int(word))
    else:
        for j in xrange(i,n+1):
            swap(i,j)
            permute(i+1,n)
            swap(i,j)

permute(0,len(word)-1)
#print array
print sum(array)

print time.time() - start
