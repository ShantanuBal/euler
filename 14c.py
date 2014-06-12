max = 1000000
collatz = []
save = 0
result = 0

for n in range(2,max):
    collatz.append(n)
    while n:
        if n == 1:
            break
        elif n%2 == 0:
            n = n / 2
            collatz.append(n)
        else:
            n = n * 3 + 1
            collatz.append(n)
    if save < len(collatz):
        save = len(collatz)
        result = collatz[0]
    collatz = []

print('Result=', result)
