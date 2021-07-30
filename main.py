from flask import Flask, jsonify # jsonify converts the output in readable generalized json format
import db
from datetime import datetime as dt

#---------------------------------------------------------------------------------------------

app = Flask(__name__)

#---------------------------------------------------------------------------------------------

@app.route('/', methods = ['GET', 'POST'])
def home():
    return '''Welcome to Prime Number Generator API<br><br>
    Append /prime/n1/n2 in the current url and replace n1 and n2 by two numbers to get all prime numbers in that range<br><br>
    Append /fetch in the current url to get all the records'''


@app.route('/prime/<int:n1>/<int:n2>', methods = ['GET'])
def prime(n1, n2):
    prime_no = []
    starttime = dt.now()    #recording start time
    if(n1 > 0 and n2 > 0):  #Checking whether the input is greater than 0
        if(n1 >= n2):
            return jsonify({'error':'First value cannot be greater than or equal to second value'})
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

            status = db.insert(starttime, n1, n2, time_elapsed, total_values)
            
            return jsonify({'range': str(n1)+'-'+str(n2), 'prime_values': prime_no, 'db_status': status})
    else:
        return jsonify({'error':'0 or negative values detected. Please enter values greater than 0'})



@app.route('/fetch', methods = ['GET'])
def fetch():
    output = db.fetch_records()

    result={}

    for i in output:
        result.update({'data'+str(output.index(i)+1):{'timestamp': i[0], 'lower': i[1], 'upper': i[2], 'elapsed time': i[3], 'output length': i[4]}})

    return jsonify({'record': result})

#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)