import datetime
start = datetime.datetime.now()

i = 40
prod = 1
while i > 20:
    prod = prod * i
    i -= 1
i = 20
while i > 0:
    prod = prod / i
    i -= 1

print prod
print datetime.datetime.now() - start
