def decimalToBinary(decimalNo):
    bit = [] #list to store the converted decimal into binary 

    for i in range (8): #running loop 8 times in order to convert the number into 8 bits
        remainder = decimalNo%2 #finding remainder
        bit.append(remainder) #adding remainder to list
        decimalNo = decimalNo//2 #floor division to move to the next calculation
    return bit #return the list 

        
