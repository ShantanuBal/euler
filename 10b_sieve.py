marked = [0] * 10
value = 3
s = 2
while value < 10:
    if marked[value] == 0:
        s += value
        i = value
        while i < 10:
            marked[i] = 1
            i += value
    value += 2
print "marked: ", marked
print "value", value
print "s",s
