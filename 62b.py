import time, pdb, math
start = time.time()

cubes, word, count, checker = {}, "", 0, []
for i in xrange(1,10000):
    cube = i*i*i
    length = len(str(cube))
    if length not in cubes:
        cubes[length] = [cube]
    else:
        cubes[length].append(cube)

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


def permute(k):
    for j in xrange(1,len(word)):
        swap(k%(j+1),j)
        k = k/(j+1)

digits = 8
for each in cubes[digits]:
    count = 0
    checker = []
    for i in xrange(0,math.factorial(digits)):
        word = str(each)
        permute(i)
        if word in checker or word[0] == '0':
            continue
        rem = (int(word) ** (1/3.0)) % 1
        if rem == 0 or str(rem) == '1.0':
            count += 1
            checker.append(word)
    print each, count, checker
    if count == 3:
        break

print time.time() - start
