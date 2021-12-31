import mysql.connector



def connection():
    dataBase = mysql.connector.connect( host = "192.168.0.102",user = "Gaurav",passwd = "password123",database = "test" ) 
    return dataBase

def insert(id,name):
            conn = connection()
            mycursor =conn.cursor()
            sql = "INSERT INTO student (id,Name) VALUES (%s, %s)"
            val = (id,name)
            mycursor.execute(sql, val)
            conn.commit()
            return "Success"


            