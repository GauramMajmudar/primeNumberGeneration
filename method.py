from datetime import datetime as dt
import db

def get_prime_1(n1, n2):
    prime_no = []
    starttime = dt.now()    #recording start time
    if(n1 > 0 and n2 > 0):
        if(n1 >= n2):
            return {'error': "First value cannot be greater than or equal to second value"}
        else:
            for i in range(n1, n2 + 1): 
                count = 2
                for j in range(2, (i//2)+1):
                    if((i % j) == 0):
                        count += 1
                if(count <= 2):
                    prime_no.append(i)
            
            #time.sleep(5) #WITHOUT DELAY THE PROGRAM RETURNS 0 REAL ELAPSED TIME EVEN IN MILLI/MICRO SECONDS
            
            time_elapsed = dt.strptime(dt.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f") - dt.strptime(starttime.strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
            #OUTPUT OF ABOVE CODE RESULTS IN DIFFERENCE BETWEEN START AND END TIME OF LOGIC IN TIMEDELTA DATA TYPE
            
            time_elapsed = str(time_elapsed) #SQLITE DOES NOT SUPPORT TIMEDELTA DATA TYPE
            total_values = len(prime_no)

            status = db.insert(1, starttime, n1, n2, time_elapsed, total_values)
            
            return {'range': str(n1)+'-'+str(n2), 'prime_values': prime_no, 'db_status': status}
    else:
        return {'error': "One or both the entered values are 0 or less. Please enter values greater than 0."}

#-------------------------------------------------------------------

def get_prime_2(n1, n2):
    prime_no = []
    prime = False
    starttime = dt.now()    #recording start time
    if(n1 > 0 and n2 > 0):
        if(n1 >= n2):
            return {'error': "First value cannot be greater than or equal to second value"}
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
            
            #time.sleep(5)
            time_elapsed = dt.strptime(dt.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f") - dt.strptime(starttime.strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
            time_elapsed = str(time_elapsed)
            total_values = len(prime_no)

            status = db.insert(2, starttime, n1, n2, time_elapsed, total_values)
            
            return {'range': str(n1)+'-'+str(n2), 'prime_values': prime_no, 'db_status': status}
    else:
         return {'error': "One or both the entered values are 0 or less. Please enter values greater than 0."}
