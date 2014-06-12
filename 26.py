import datetime
start = datetime.datetime.now()

def check(character, word, rem, rem_word):
    for i in xrange(len(word)):
        if word[i] == character:
            if rem_word[i] == rem:
                return 1
    return 0

def decimal(num):
    word = ""
    rem_word = ""
    remainder = 1 % num
    while remainder != 0:
        if remainder < num:
            remainder *= 10
            continue

        character = str(remainder / num)
        rem = str(remainder % num)

        if check(character, word, rem, rem_word):
            new = ""
            for j in xrange(len(word)):
                if word[j] == character and rem_word[j] == rem:
                    word += '('
                word += word[j]
            word += ')'
            return word

        word += character
        rem_word += rem
        remainder = remainder % num
    return word

for i in xrange(2,1000):
    print i,'--->',decimal(i)

print datetime.datetime.now()-start
