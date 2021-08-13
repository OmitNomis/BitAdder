def validation(number):
   
        if (number < 0 or number>255 ): #condition for number to be a valid number
            
            while (number < 1 or number>255): # loop for repetadely asking for input incase of wrong input
                print("\n\n Invalid Input!!! ")
                number = int(input("Please Re-enter Decimal number between 0 and 255: "))
        return number# return the validated number
   
