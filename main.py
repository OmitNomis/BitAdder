import binaryAddition   #importing the module responsible for binary addition    
import validateNumber   #importing the module responsible for number validation 
import binaryConverter  #importing the module responsible for binary conversion 
import reverseNumber    #importing the module responsible for reversing a number 
        

choice = True 


while choice == True: #loop to continue asking input to the user
    success = False
    while success == False: #loop to handle the exception
        try:
              num1 = int(input("\n\nEnter first decimal Number: "))
              validatedNumber1 = validateNumber.validation(num1)
              success = True
        except:
              print("Invalid input, input a decimal number between 0 and 255") # message to be printed when there is invalid input

    success = False
    while success == False:
        try:
              num2 = int(input("\n\nEnter second decimal Number: "))
              validatedNumber2 = validateNumber.validation(num2)
              success = True
        except:
              print("Invalid input, input a decimal number between 0 and 255")# message to be printed when there is invalid input

        #converting validated number into binary
    binarynum1 = binaryConverter.decimalToBinary(validatedNumber1) 
    binarynum2 = binaryConverter.decimalToBinary(validatedNumber2)
        #reversing the binary converted number to get the actual binary value
    actualBinaryNum1 = reverseNumber.reverse(binarynum1)
    actualBinaryNum2 = reverseNumber.reverse(binarynum2)
        #binary numbers sent for addition and print the added value
    print("\n \nThe sum of two binary numbers = ",binaryAddition.addBinary(actualBinaryNum1,actualBinaryNum2))
        #condition for the user to continue/discontinue the loop
    conti=input("\n \nDo you wish to continue? (Type \"no\" in order to exit)").lower()
    if conti == "no":
        print("\n\nThank you for using the Application!!!!!") #end message after exiting the application
        break

  




