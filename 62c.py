import time, pdb, math
start = time.time()

cubes, word, count, checker = {}, "", 0, []
for i in xrange(1,100000):
    cube = i*i*i
    length = len(str(cube))
    if length not in cubes:
        cubes[length] = [cube]
    else:
        cubes[length].append(cube)

def is_perm(x,y):
    l1, l2 = [each for each in str(x)], [each for each in str(y)]
    for each in l1:
        if each in l2:
            l2.remove(each)
        else:
            return 0
    return 1

no_of_perms = 2
digits = 8; array = cubes[digits]
desc = []
for each in array:
    string = ""
    for i in xrange(10):
        string += str(i) + str(str(each).count(str(i)))
    desc.append(string+str(each))

for i in xrange(len(array)):
    count = 0
    for j in xrange(i+1, len(array)):
        if is_perm(array[i],array[j]):
            count += 1
    print array[i], count
    if count == no_of_perms:
        break

print time.time() - start
print "digits --> ", digits
for each in cubes:
    print each," ----- ", len(cubes[each])
