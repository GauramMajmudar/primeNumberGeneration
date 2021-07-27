#After updating the first logic.

def get_prime(n1, n2):   #Function definition
    prime_no = []           #list to store the output
    if(n1 > 0 and n2 > 0):  #Checking whether the input is greater than 0
        if(n1 >= n2):
            return "First value cannot be greater than or equal to second value"
        else:
            for i in range(n1, n2 + 1): 
                count = 2       #count varaible keeps track of how many numbers can divide the x (i.e i) value
                for j in range(2, i):
                    if((i % j) == 0):
                        count += 1      #increase by 1 if divisible
                if(count <= 2):
                    prime_no.append(i)    #if count is less than or equal to 2 then i is prime else not
            return prime_no
    else:
        return "One or both the entered values are 0 or less. Please enter values greater than 0."

if __name__ == "__main__":
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    print("\nOutput:", get_prime(n1, n2))

#-------------------------------------------------------------------

#First Logic

# n1 = int(input("Enter n1:"))
# n2 = int(input("Enter n2:"))

# prime_no = []

# for i in range(n1, n2 + 1):
#     count = 1
#     for j in range(1, i):
#         if((i % j) == 0):
#             count += 1
    
#     if(count <= 2):
#         prime_no.append(i)

# print("Prime numbers generated are:", prime_no)