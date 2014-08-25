import time
start = time.time()

def p075():
    N = 900
    l1 = [[2,1]]
    i = 0
    while i<len(l1):
        a,b,c = 2*l1[i][0]-l1[i][1], 2*l1[i][0]+l1[i][1], l1[i][0]+2*l1[i][1]
        if a < N:
            l1.append([a, l1[i][0]])
        if b < N:
            l1.append([b, l1[i][0]])
        if c < N:
            l1.append([c, l1[i][1]])
        i += 1

    dict = [0]*1500001

    for each in l1:
        a, b, c = each[0]**2 - each[1]**2, 2*each[0]*each[1], each[0]**2 + each[1]**2
        i = 1
        while i*(a+b+c) <= 1500000:
            dict[i*(a+b+c)] += 1
            i += 1

    count = 0
    for each in range(len(dict)):
        if dict[each] == 1:
            count += 1
    return count

print p075()
print time.time() - start
