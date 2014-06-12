import time
start = time.time()

num = ''
i = 0
while i < 190000:
    i += 1
    num += str(i)

answer = 1
for i in [1,10,100,1000,10000,100000,1000000]:
    answer *= int(num[i-1])
print answer

print time.time() - start
