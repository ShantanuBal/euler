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

no_of_perms = 4
digits = 12; array = cubes[digits]
desc = []
for each in array:
    string = ""
    for i in xrange(10):
        string += str(i) + str(str(each).count(str(i)))
    desc.append(string+str(each))

desc.sort()
for i in xrange(len(desc)-no_of_perms):
    for j in xrange(i+1, i+no_of_perms+1):
        if desc[j][:-1*digits] != desc[i][:-1*digits]:
            break
    else:
        print desc[i][-1*digits:]
        for j in xrange(i+1, i+no_of_perms+1):
            print desc[j][-1*digits:]
        print '\n',

print time.time() - start
