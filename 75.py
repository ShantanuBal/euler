import time, math
start = time.time()

N= 1500000
i = 2
sq = []
while i**2 < N:
    sq.append(i**2)
    i += 1

for i in range(1,len(sq)):
    for j in range(0,i):
        if math.sqrt(sq[i]+sq[j]) % 1 == 0:
            print math.sqrt(sq[j]), math.sqrt(sq[i]), math.sqrt(sq[i]+sq[j])
print time.time() - start
