
def halfAdder(a, b):
    sum = a^b #finding the sum of the two binary digits
    cOut = a & b #finding the carry when 2 digits are added
    return cOut,sum 

def fullAdder(a, b, cIn):
    #calling the half adder twice with values to make a full adder
    c1,s1 = halfAdder(cIn,a) 
    c2,sum = halfAdder(s1,b)
    carry = c1 | c2 # finding the carry 
    return carry,sum #returning the carry as well as the sum


def addBinary(a,b):
    result = [] #list to store added binary digits
    carry = 0 #initialization of carry
    finalResult = "" #string to store the final result
    for i in range (len(a)-1,-1,-1): #loop that runs backwards
        carry,sum = fullAdder(a[i],b[i],carry) #calling full adder with the two digits and carry as 0
        result.insert(0,sum) #adding the added digit to 0 index in the list
    for each in result: # loop to turn the list into string
        finalResult += str(each)
    return int(finalResult) #returning string as int so that exact value is sent (excluding 0s)
    
