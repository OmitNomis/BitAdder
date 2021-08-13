def reverse(binaryNumber):
    actualBinary = [] #list to store the reversed number
    for i in range (len(binaryNumber)-1,-1,-1): #running the loop backwards
        actualBinary.append(binaryNumber[i]) #adding the digits (backwards) in the new list
    return actualBinary #returning the reversed list
    
