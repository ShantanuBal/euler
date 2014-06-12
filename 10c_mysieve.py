import datetime
start = datetime.datetime.now()

n = 100000
sieve = [0] * n
prime = 2
store = []
while prime < n:
    i = prime + prime
    while i < n:
        sieve[i] = 1
        i += prime
    prime += 1

array = []
i = 2
while i < len(sieve):
    if sieve[i] == 0:
        array.append(i)
    i += 1

print sum(array)

end = datetime.datetime.now()
print end - start
