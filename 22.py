f = open('/Users/shantanubal/Downloads/names.txt','r+')
text = f.read()
word = ""
array = []
for each in text:
    if each == ",":
        array.append(str(word))
        word = ""
    elif each != " " and each != '"':
        word += each
array.append(word)
array.sort()

score = []
value = 0
for each in array:
    for every in each:
        value += ord(every)-64
    score.append(value)
    value = 0

new_score = []
for i in range(0, len(array)):
    new_score.append((i+1)*score[i])


for i in range(0, len(array)/2):
    print array[i],'...',score[i],'...',new_score[i]
print sum(new_score)
