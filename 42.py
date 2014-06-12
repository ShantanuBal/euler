import time
start = time.time()

triangle = []
for i in xrange(1,1000):
    triangle.append(i*(i+1)/2)

f = open("/Users/shantanubal/Downloads/words.txt","r+")
text = f.read()
array = []
word = ''
for each in text:
    if each == ',':
        array.append(word[1:-1])
        word = ''
    else:
        word += each
array.append(word[1:-1])

count = 0
for each in array:
    sum = 0
    for every in each:
        sum += ord(every)-64
    if sum in triangle:
        count += 1
print count

print time.time() - start
