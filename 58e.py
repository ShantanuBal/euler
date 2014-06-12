import time, pdb, math, random
start = time.time()

def is_prime(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    ''' first we want to express n as : 2^s * r ( were r is odd ) '''
    
    ''' the odd part of the number '''
    oddPartOfNumber = number - 1
    
    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0
    
    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 
     
    '''
    since there are number that are cases of "strong liar" we 
    need to check more then one number
    '''
    for time in range(3):
        
        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        
        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''     
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False
            
    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True 


def is_prime_2(x):
    if x%6 not in [1,5]:
        return 0
    for i in xrange(3,int(math.sqrt(x)),2):
        if x%i == 0:
            return 0
    return 1

def is_prime_3(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num%2 or not num%3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):   
        if not num%i or not num%(i + 2):
            return False
    return True

i = 3
primes = 3
print "SIDE DIAGS PRIMES RATIO"
while 1:
    #print i,"",2*i-1," ",primes," ",float(primes)/float(2*i-1)
    if float(primes) < .1 * float(2*i-1):
        break
    if is_prime(i**2+i+1):
        primes += 1
        last = i**2+i+1
    if is_prime(i**2+2*i+2):
        primes += 1
        last = i**2+2*i+2
    if is_prime(i**2+3*i+3):
        primes += 1
        last = i**2+3*i+3
    i += 2
print i
print time.time() - start
