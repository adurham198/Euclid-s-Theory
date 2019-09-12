#Anton Durham
#Desc: This is a program designed to test Euclid's theory 
#1/24/209

def isprime(i):

    
    if (i == 0 or i == 1):
            #nothing
            return False
            
    elif (i == 2):
            return True
        #these are base cases
    else:
            for k in range (2, i // 2 + 1):
                #the double // is for returning as an integer
                if (i % k == 0):
                      return False
            #this for loop checks if the number has any factors that would render the number non-prime
                
    return True
       

    
def findprimefacs(x):
#this function is to find prime factors 
    print(x," is divisible by ")
    
    for i in range(1, x + 1):
           if x % i == 0 and i!=1 and i!=x:
               
               print(i)
              

           
def makeprimelist():
#this function makes a list of prime numbers
#between 1- n numbers by looping through and
#looking for all prime numbers 
    primeornot = False
    primes = []
    
    for i in range ( 0, 26):
            primeornot = isprime(i)
            if (primeornot == False):
                print("")
            elif (primeornot == True):
                primes.append(i)
    return primes
    
def euclid(primes):
    #print (primes)
    #primes is our list of prime numbers from 1-25
    primeornot = False
   # sets = []
    for i in range(0, len(primes)+1):
        setout = []
        val = 1
        
        for j in range( 0, i):
            if( i != j ):
                
                setout.append(val+1)
                val = val * primes[j]
        vals = []
        for j in range( 0, i):
            if( i != j ):
                vals.append(primes[j])
                
        primeornot = isprime(val+1)
        #send the number multiplied by all the primes in our set +1 to check if it's prime 
        print("==========================")
        print("Test ", i)
        print("==========================")
        print(vals)
        print(val+1)
        print("Euclid's theory is correct")
        if(primeornot==True):
        
            print(val+1, " is a prime number that is currently not on our list")
        elif(primeornot==False):

            findprimefacs(val+1)
        print("==========================")
        #sets.append(setout)
        
            
    
    #print(sets)

something=makeprimelist()

euclid(something)
