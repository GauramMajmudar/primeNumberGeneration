from flask import Flask, jsonify # jsonify converts the output in readable generalized json format
from method import get_prime_1, get_prime_2
import db

#---------------------------------------------------------------------------------------------

app = Flask(__name__)

#---------------------------------------------------------------------------------------------

@app.route('/', methods = ['GET', 'POST'])
def home():
    #output = db.create() #Need to run only once when database file is not created.
    return '''Welcome to Prime Number Generator API<br><br>
    Append /prime1/n1/n2 in the current url to use the first algorithm and replace n1 and n2 by two numbers to get all prime numbers in that range<br><br>
    Append /prime2/n1/n2 in the current url to use the second algorithm and replace n1 and n2 by two numbers to get all prime numbers in that range<br><br>
    Append /fetch in the current url to get all the records'''


@app.route('/prime1/<int:n1>/<int:n2>', methods = ['GET'])
def prime1(n1, n2):
    result = get_prime_1(n1, n2)
    return jsonify(result)


@app.route('/prime2/<int:n1>/<int:n2>', methods = ['GET'])
def prime2(n1, n2):
    result = get_prime_2(n1, n2)
    return jsonify(result)


@app.route('/fetch', methods = ['GET'])
def fetch():
    output = db.fetch_records()

    result={}

    for i in output:
        result.update({'data'+str(output.index(i)+1):{'algorithm': i[0], 'timestamp': i[1], 'lower': i[2], 'upper': i[3], 'elapsed time': i[4], 'output length': i[5]}})

    return jsonify({'record': result})

#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)