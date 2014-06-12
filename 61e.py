import time, pdb
start = time.time()

tri, sqr, pen, hex, hep, oct = [], [], [], [], [], []

def check(x,array):
    if len(str(x)) == 4:
        array.append(str(x)[:2])
        array.append(str(x)[-2:])

i = 1
while True:
    a = i * (i+1) / 2; b = i * i; c = i * (3*i - 1) / 2; d = i * (2*i - 1); e = i * (5*i - 3) / 2; f = i * (3*i - 2)
    check(a,tri); check(b,sqr); check(c,pen); check(d,hex);check(e,hep); check(f,oct)
    if len(str(a)) > 4 and len(str(b)) > 4 and len(str(c)) > 4 and len(str(d)) > 4 and len(str(e)) > 4 and len(str(f)) > 4:
        break
    i += 1
#print len(tri), len(sqr), len(pen), len(hex), len(hep), len(oct)

def find_pos(x,array):
    #pdb.set_trace()
    pos = [array[(array[::2].index(x)*2)+1]]
    i = (array[::2].index(x) * 2) + 2
    while i < len(array)-1:
        if array[i] == x:
            pos.append(array[i+1])
        i += 2
    return pos

def layer1(x):
    l1 = []
    if x in sqr[::2]:
        pos = find_pos(x,sqr)
        for i in pos:
            l1.append([x]+[4,i])
    if x in tri[::2]:
        pos = find_pos(x,tri)
        for i in pos:
            l1.append([x]+[3,i])
    return l1

def layer2(l1):
    l2 = []
    for each in l1:
        if 4 not in each and each[-1] in sqr[::2]:
            pos = find_pos(each[-1],sqr)
            for i in pos:
                l2.append(each+[4,i])
        if 3 not in each and each[-1] in tri[::2]:
            pos = find_pos(each[-1],tri)
            for i in pos:
                l2.append(each+[3,i])
    return l2                

i = 1
while i<len(pen):
    l1 = layer1(pen[i])
    l2 = layer2(l1)
    for each in l2:
        print each
        if each[-1] == pen[i-1]:
            print pen[i-1],pen[i], pen[i],each[2], each[2],each[4]
            print time.time() - start
            exit(0)
    i += 2
