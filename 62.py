import time, pdb
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

def permute(i,n):
    global count
    if i==n:
        if word in checker or word[0] == '0':
            return
        rem = (int(word) ** (1/3.0)) % 1
        if rem == 0 or str(rem) == '1.0':
            count += 1
            checker.append(word)
    else:
        for j in range(i,n+1):
            swap(i,j)
            permute(i+1,n)
            swap(i,j)

digits = 8
for each in cubes[digits]:
    word = str(each)
    count = 0
    checker = []
    permute(0,digits-1)
    print each, count, checker
    if count == 3:
        break

print time.time() - start
