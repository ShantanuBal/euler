import time
start = time.time()

def pb075(N=1500000):
    t0 = lambda m, n : (2 * m - n, m)
    t1 = lambda m, n : (2 * m + n, m)
    t2 = lambda m, n : (m + 2 * n, n)
    functions = (t0, t1, t2)
    couples = [(2, 1)]
    perimeters = [0] * (N + 1)
    for i in range(12, N + 1, 12):
        perimeters[i] += 1
    while couples:
        newcouples = []
        for (m, n) in couples:
            for i in range(3):
                u, v = functions[i](m, n)
                L = 2 * u * (u + v)
                if L <= N:
                    newcouples.append((u, v))
                    for i in range(L, N + 1, L):
                        perimeters[i] += 1
        couples = newcouples
    rep = [i for i in range(N + 1) if perimeters[i] == 1]
    #print(rep)
    return(len(rep))

print pb075()
print time.time() - start
