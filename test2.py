import time
start = time.time()

list = []
for a in range(1000000)[::-1]:
    print a
    list.append(a)

list.sort()
print time.time() - start
