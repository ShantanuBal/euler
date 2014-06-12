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
tri.append('66'); tri.append('11')
sqr.append('55'); sqr.append('66')
pen.append('44'); pen.append('55')
hex.append('33'); hex.append('44')
hep.append('22'); hep.append('33')
oct.append('11'); oct.append('22')

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


def is_present(x):
    present = []
    if x in hep[::2]:
        present.append([7,find_pos(x,hep)])
    

i = 1
while i<len(oct):
    oct_present = is_present([oct[i]])
    if oct[i] in hep[::2]:
        print oct[i]
        h_pos = find_pos(oct[i],hep)
        for h in h_pos:
            if h in hex[::2]:
                print oct[i], h
                h2_pos = find_pos(h,hex)
                for h2 in h2_pos:
                    if h2 in pen[::2]:
                        print oct[i], h, h2
                        p_pos = find_pos(h2,pen)
                        for p in p_pos:
                            if p in sqr[::2]:
                                print oct[i], h, h2, p
                                s_pos = find_pos(p,sqr)
                                for s in s_pos:
                                    if s in tri[::2]:
                                        print oct[i], h, h2, p, s
                                        t_pos = find_pos(s,tri)
                                        for t in t_pos:
                                            if t == oct[i-1]:
                                                print oct[i-1]+oct[i]," ",oct[i]+h," ",h+h2," ",h2+p," ",p+s," ",s+oct[i-1]
                                                print time.time() - start
                                                exit(0)
    i += 2
