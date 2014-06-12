import time
start = time.time()

f = open('59.txt','r+')
text = f.read()
list = []
word = ''
for each in text:
    if each == ',':
        list.append(int(word))
        word = ''
    else:
        word += each
list.append(int(word))

def apply(a,b,c):
    tracker = 1
    message = ""
    for each in list:
        if len(message) > 10 and " " not in message:
            break
        if tracker == 1:
            message += chr(a ^ each)
            tracker += 1
        elif tracker == 2:
            message += chr(b ^ each)
            tracker += 1
        else:
            message += chr(c ^ each)
            tracker = 1
    return message

decoded = []
for a in xrange(97,123):
    for b in xrange(97,123):
        for c in xrange(97,123):
            message = apply(a,b,c)
            if ' the ' in message and ' and ' in message and ' a ':
                print message
                sum = 0
                for each in message:
                    sum += ord(each)
                print chr(a)+chr(b)+chr(c)
                print sum
                print time.time() - start
            decoded.append([chr(a)+chr(b)+chr(c),message])

print time.time() - start
