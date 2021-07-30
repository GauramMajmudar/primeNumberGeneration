import sqlite3


#-------------------------TO CREATE NEW TABLE------------------------------------------------
def create():
    connection = sqlite3.connect('entry.db') #CONNECTION OBJECT CREATED
    conn = connection.cursor() #CONNECTION INSTANCE CREATED
    conn.execute('''
        CREATE TABLE prime (
            timestamp blob,
            lower integer,
            upper integer,
            time_elapsed blob,
            total_values integer
        )
    ''')
    connection.commit() #DATABASE TRANSACTION COMMIT
    connection.close() #DATABASE CONNECTION CLOSED

    return True

#-------------------------INSERT DATA INTO TABLE------------------------------------------------
def insert(starttime, n1, n2, time_elapsed, total_values):
    connection = sqlite3.connect('entry.db')
    conn = connection.cursor()
    conn.execute('INSERT INTO prime VALUES (?,?,?,?,?)', (starttime, n1, n2, time_elapsed, total_values))
    connection.commit()
    connection.close()

    return True

#-------------------------FETCH ALL RECORDS FROM THE TABLE------------------------------------------------
def fetch_records():
    connection = sqlite3.connect('entry.db')
    conn = connection.cursor()
    conn.execute('SELECT * FROM prime')
    output = conn.fetchall()
    connection.commit()
    connection.close()

    return output