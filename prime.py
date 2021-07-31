from datetime import datetime as dt
import db

def get_prime_1(n1, n2):   #Function definition
    prime_no = []           #list to store the output
    if(n1 > 0 and n2 > 0):  #Checking whether the input is greater than 0
        if(n1 >= n2):
            return "First value cannot be greater than or equal to second value"
        else:
            for i in range(n1, n2 + 1): 
                count = 2       #count varaible keeps track of how many numbers can divide the x (i.e i) value
                for j in range(2, (i//2)+1):
                    if((i % j) == 0):
                        count += 1      #increase by 1 if divisible
                if(count <= 2):
                    prime_no.append(i)    #if count is less than or equal to 2 then i is prime else not
            
            return prime_no
    else:
        return "One or both the entered values are 0 or less. Please enter values greater than 0."

#-------------------------------------------------------------------

def get_prime_2(n1, n2):
    prime_no = []
    prime = False
    if(n1 > 0 and n2 > 0):
        if(n1 >= n2):
            return "First value cannot be greater than or equal to second value"
        else:
            for i in range(n1, n2 + 1):
                val = i ** 0.5 
                if((val % int(val)) == 0): #checking whether the number is a perfect square
                    prime = False
                else:
                    if (i in [2, 3, 5, 7]):
                        prime = True
                    else:
                        for j in [2, 3, 5, 7]: #checking whether the number is divisible by first 4 primes
                            if((i % j) == 0):
                                prime = False
                                break
                            else:
                                prime = True
                        
                        if(i > 10 and prime == True): #if number greater than 10 and not divisible by first 4 primes then check for number/2
                            for j in range(2, (i//2)+1):
                                if(i % j == 0):
                                    prime = False
                                    break
                
                if(prime):
                    prime_no.append(i)

            return prime_no
    else:
         return "One or both the entered values are 0 or less. Please enter values greater than 0."

#-------------------------------------------------------------------


if __name__ == "__main__":
    print("\nThere are 2 algorithms available to generate prime numbers in given range")
    print("\nEnter the range first and then select your algorithm by entering 1 or 2.")
    n1 = int(input("\nEnter n1:"))
    n2 = int(input("\nEnter n2:"))
    choice = input("\nEnter your algorithm choice: ")

    if(choice == '1'):
        print("\nOutput:", get_prime_1(n1, n2))
    elif(choice == '2'):
        print("\nOutput:", get_prime_2(n1, n2))
    else:
        print("\nInvalid Input")

#-------------------------------------------------------------------