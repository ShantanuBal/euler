dict = {1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
1000:'one thousand'}

word = ""
i = 1
while i < 1001:
    text = str(i)
    if len(text) == 1:
        word += dict[i] + '\n'
    elif len(text) == 2:
        if i in [10,11,12,13,14,15,16,17,18,19]:
            word += dict[i] + '\n'
        else:                
            word += dict[int(text[0]+'0')]
            if int(text[1]) > 0:
                word += dict[int(text[1])] + '\n'
    elif len(text) == 3:
        word += dict[int(text[0])] + 'hundred'
        if int(text[1]+text[2]) in [10,11,12,13,14,15,16,17,18,19]:
            word += 'and' + dict[int(text[1]+text[2])] + '\n'
        else:   
            if text[1] != '0' or int(text[2]) > 0:
                word += 'and'
            if text[1] != '0':             
                word += dict[int(text[1]+'0')]
            if int(text[2]) > 0:
                word += dict[int(text[2])]
            word += '\n'
    elif len(text) == 4:
        word += 'one thousand'
    i += 1
print word

count = 0
for each in word:
    if each not in ['\n',' ','  ']:
        count += 1
print count
