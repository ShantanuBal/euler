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

def find_pos(x,array):
    #pdb.set_trace()
    pos = [array[(array[::2].index(x)*2)+1]]
    i = (array[::2].index(x) * 2) + 2
    while i < len(array)-1:
        if array[i] == x:
            pos.append(array[i+1])
        i += 2
    return pos

def new_layer(l1):
    l2 = []
    for each in l1:
        if 7 not in each and each[-1] in hep[::2]:
            pos = find_pos(each[-1],hep)
            for i in pos:
                l2.append(each+[7,i])
        if 6 not in each and each[-1] in hex[::2]:
            pos = find_pos(each[-1],hex)
            for i in pos:
                l2.append(each+[6,i])
        if 5 not in each and each[-1] in pen[::2]:
            pos = find_pos(each[-1],pen)
            for i in pos:
                l2.append(each+[5,i])
        if 4 not in each and each[-1] in sqr[::2]:
            pos = find_pos(each[-1],sqr)
            for i in pos:
                l2.append(each+[4,i])
        if 3 not in each and each[-1] in tri[::2]:
            pos = find_pos(each[-1],tri)
            for i in pos:
                l2.append(each+[3,i])
    return l2                

#pdb.set_trace()
j = 1
while j<len(oct):
    l1 = new_layer([[oct[j]]])
    l2 = new_layer(l1)
    l3 = new_layer(l2)
    l4 = new_layer(l3)
    l5 = new_layer(l4)
    for each in l5:
        if each[-1] == oct[j-1]:
            print int(oct[j-1]+oct[j])+int(oct[j]+each[2])+int(each[2]+each[4])+ int(each[4]+each[6])+int(each[6]+each[8])+int(each[8]+each[10])
            print time.time() - start
            exit(0)
    j += 2
print oct
