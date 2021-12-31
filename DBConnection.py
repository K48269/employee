import mysql.connector
from cryptography.fernet import Fernet


def connection():
    dataBase = mysql.connector.connect( host = "localhost",user = "root",passwd ="Soft#2021",database = "main" ) 
    return dataBase



class DB:
    def select_with_id(self,id):
        database=connection()
        cursorObject = database.cursor()
        sql="select * from login_passwords where id= %s"
        cursorObject.execute(sql,(id,))
        my_result=cursorObject.fetchall()
        return my_result

    def insert(self,id,name,mno,email):
            conn = connection()
            mycursor =conn.cursor()
            sql = "INSERT INTO Employee_info (id,name,Mobile_number,Email_id) VALUES (%s, %s, %s, %s)"
            val = (id,name,mno,email)
            mycursor.execute(sql, val)
            conn.commit()
            return "Success"
        

    def login_credentails(self,id,key,enpassword):
            conn = connection()
            mycursor =conn.cursor()
            sql = "INSERT INTO login_passwords (id,e_key,p_key) VALUES (%s, %s, %s)"
            val = (id,key,enpassword)
            mycursor.execute(sql, val)
            conn.commit()
            return "Success"

    def select_values(self,id):
        database=connection()
        cursorObject = database.cursor()
        sql='select a.id,a.name,a.Mobile_number,a.Email_id,b.e_key,b.p_key from employee_info a inner join login_passwords b on a.id=b.id where a.id=%s'
        cursorObject.execute(sql,(id,))
        my_result=cursorObject.fetchall()
        return my_result
    
                 







