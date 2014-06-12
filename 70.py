import time
start = time.time()

N=10000000
Phi=list(xrange(N))

for i in xrange(2,N):
    if Phi[i]==i:
        for j in range(2*i, len(Phi),i):
            Phi[j]=Phi[j]*(i-1)/i #Phi[j]//i*(i-1)
        Phi[i]-=1

def is_perm(a,b):
    if a.sort() == b.sort():
        return 1
    return 0

min_ratio = 2
perms = []
for i in xrange(1000000,N):
    if is_perm(list(str(i)),list(str(Phi[i]))):
        perms.append([i,Phi[i]])
        ratio = float(i)/float(Phi[i]) 
        print i, Phi[i], ratio
        if ratio < min_ratio:
            min_ratio = ratio
            min_n = i

print min_n
print time.time() - start
