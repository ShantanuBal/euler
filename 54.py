import time,pdb
start = time.time()

def high_card(a,b):
    n1, n2 = [],[]
    for each in a:
        n1.append(each[:-1])
    for each in b:
        n2.append(each[:-1])
    #pdb.set_trace()
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if each in n1 and each in n2:
            continue
        elif each in n1:
            return 1
        elif each in n2:
            return 0

def royal_flush(array):
    n, suit = [],[]
    for each in array:
        n.append(each[:-1])
        suit.append(each[-1])
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4] and 'T' in n and 'J' in n and 'Q' in n and 'K' in n and 'A' in n:
        return 1
    return 0

def straight_flush(array):
    n,suit = [],[]
    for each in array:
        n.append(each[:-1])
        suit.append(each[-1])
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
        i = 0
        list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        while i < len(n) - 4:
            if list[i] in n and list[i+1] in n and list[i+2] in n and list[i+3] in n and list[i+4] in n:
                return list[i]
            i += 1
    return 0

def four_of_a_kind(array):
    n = []
    for each in array:
        n.append(each[:-1])
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if n.count(each) == 4:
            return each
    return 0

def full_house(array):
    n = []
    for each in array:
        n.append(each[:-1])
    three, two = 0,0
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if n.count(each) == 3:
            three = each
        if n.count(each) == 2:
            two = each
    if three and two:
        return [three,two]
    return 0

def flush(array):
    suit = []
    for each in array:
        suit.append(each[-1])
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:    
        return 1    
    return 0

def straight(array):
    n = []
    for each in array:
        n.append(each[:-1])
    list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    i = 0
    while i < len(list)-4:
        if list[i] in n and list[i+1] in n and list[i+2] in n and list[i+3] in n and list[i+4] in n:
            return 1
        i += 1
    return 0

def three_of_a_kind(array):
    n = []
    for each in array:
        n.append(each[:-1])
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if n.count(each) == 3:
            return 1
    return 0

def two_pairs(array):
    n = []
    for each in array:
        n.append(each[:-1])
    count = 0
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if n.count(each) == 2:
            count += 1
    if count == 2:
        return 1
    return 0

def one_pair(array):
    n = []
    for each in array:
        n.append(each[:-1])
    for each in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        if n.count(each) == 2:
            #print "one pair --> ",each
            return each
    return 0

def check(a,b):
    #check for royal flush
    if royal_flush(a):
        return 1
    elif royal_flush(b):
        return 0
    elif straight_flush(a):
        if straight_flush(b):
            l1, l2 = straight_flush(a), straight_flush(b)
            list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
            if list.index(l1)<list.index(l2):
                return 1
            elif list.index(l1)>list.index(l2):
                return 0
            elif high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1  
    elif straight_flush(b):
        return 0  
    elif four_of_a_kind(a):
        if four_of_a_kind(b):
            l1, l2 = four_of_a_kind(a), four_of_a_kind(b)
            list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
            if list.index(l1)<list.index(l2):
                return 1
            elif list.index(l1)>list.index(l2):
                return 0
            elif high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif four_of_a_kind(b):
        return 0
    elif full_house(a):
        if full_house(b):
            l1, l2 = full_house(a), full_house(b)
            list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
            if list.index(l1[0])<list.index(l2[0]):
                return 1
            elif list.index(l1[0])>list.index(l2[0]):
                return 0
            elif list.index(l1[1])<list.index(l2[1]):
                return 1
            elif list.index(l1[1])>list.index(l2[1]):
                return 0
            elif high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif full_house(b):
        return 0
    elif flush(a):
        if flush(b):
            if high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif flush(b):
        return 0
    elif straight(a):
        if straight(b):
            if high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif straight(b):
        return 0
    elif three_of_a_kind(a):
        if three_of_a_kind(b):
            if high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif three_of_a_kind(b):
        return 0    
    elif two_pairs(a):
        if two_pairs(b):
            if high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif two_pairs(b):
        return 0
    elif one_pair(a):
        number1 = one_pair(a)
        if one_pair(b):
            number2 = one_pair(b)
            list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
            if list.index(number1)<list.index(number2):
                return 1
            elif list.index(number1)>list.index(number2):
                return 0
            elif high_card(a,b):
                return 1
            else:
                return 0
        else:
            return 1
    elif one_pair(b):
        return 0
    elif high_card(a,b):
        return 1
    else:
        return 0
    
p1, p2 = [],[]
f = open('/Users/shantanubal/euler/poker.txt','r+')
text = f.read()
f.close()

count = 0
string = ''
for each in text:
    if each == '\n':
        p1.append([string[0:2],string[3:5],string[6:8],string[9:11],string[12:14]])
        p2.append([string[15:17],string[18:20],string[21:23],string[24:26],string[27:29]])
        string = ''
    else:
        string += each

p1_hands, p2_hands = 0,0

for i in xrange(len(p1)):
    print i," --> ",p1[i]," -- ",p2[i],"     ",p1_hands," -- ",p2_hands
    if check(p1[i],p2[i]):
        p1_hands += 1
    else:
        p2_hands += 1

print p1_hands," -- ",p2_hands
print time.time() - start
