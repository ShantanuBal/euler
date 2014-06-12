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

#for p in pen[1::2]:
i = 1
while i<len(pen):
    if pen[i] in sqr[::2]:
        print pen[i]
        s_pos = find_pos(pen[i],sqr)
        for s in s_pos:
            if s in tri[::2]:
                print pen[i], s
                t_pos = find_pos(s,tri)
                for t in t_pos:
                    if t == pen[i-1]:
                        print pen[i-1]+pen[i]," ",pen[i]+s," ",s+pen[i-1]
                        print time.time() - start
                        exit(0)
    i += 2
