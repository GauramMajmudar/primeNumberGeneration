import sqlite3, time
from datetime import datetime as dt

#-------------------------TO CREATE NEW TABLE------------------------------------------------
# connection = sqlite3.connect('entry.db')
# conn = connection.cursor()
# conn.execute('''
#         CREATE TABLE prime (
#             timestamp blob,
#             lower integer,
#             upper integer,
#             time_elapsed blob,
#             total_values integer
#         )
# ''')
# connection.commit()
# connection.close()
#---------------------------------------------------------------------------------------------

def get_prime(n1, n2):   #Function definition
    prime_no = []           #list to store the output
    starttime = dt.now()
    
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
            
            
            #time.sleep(5) #WITHOUT DELAY THE PROGRAM RETURNS 0 REAL ELAPSED TIME EVEN IN MILLI/MICRO SECONDS
            time_elapsed = dt.strptime(dt.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f") - dt.strptime(starttime.strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
            #OUTPUT OF ABOVE CODE RESULTS IN DIFFERENCE BETWEEN START AND END TIME OF LOGIC IN TIMEDELTA DATA TYPE
            time_elapsed = str(time_elapsed) #SQLITE DOES NOT SUPPORT TIMEDELTA DATA TYPE
            
            total_values = len(prime_no)
            
            connection = sqlite3.connect('entry.db') #CONNECTION OBJECT CREATED
            conn = connection.cursor() #CONNECTION INSTANCE CREATED
            conn.execute('INSERT INTO prime VALUES (?,?,?,?,?)', (starttime, n1, n2, time_elapsed, total_values))
            connection.commit() #DATABASE TRANSACTION COMMIT
            connection.close()  #DATABASE CONNECTION CLOSED
            
            return prime_no
    else:
        return "One or both the entered values are 0 or less. Please enter values greater than 0."


#-------------------------TO FETCH ALL DATA------------------------------------------------
# connection = sqlite3.connect('entry.db')
# conn = connection.cursor()

# conn.execute('SELECT * FROM prime')
# print(conn.fetchall())
# connection.commit()
# connection.close()

#-------------------------FUCNTION CALL TO MAIN LOGIC------------------------------------------------
# print(get_prime(2, 50))