
from os import name
from flask import Flask,render_template,request,send_file
import sqlite3
from reportlab.pdfgen import canvas

name=""
mon=""
def pdf():
   pdf=canvas.Canvas("kiranpdf")
   pdf.save()

def insert_values_to_data_base(firstname,lastname,email,password):
   con=sqlite3.connect("student_data_base.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS customer(first_name TEXT,password TEXT,Mobile TEXT,Email TEXT)")
   cur.execute("INSERT INTO customer VALUES(?,?,?,?)",(firstname,lastname,email,password))
   con.commit()

def insert_values_to_data_base_Employee(firstname,lastname,email,password,dob,total,absent):
   con=sqlite3.connect("student_data_base.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS Employee(first_name TEXT,password TEXT,Mobile TEXT,Email TEXT,DateOfBirth TEXT,Total INTEGER,Absent INTEGER)")
   cur.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?,?)",(firstname,lastname,email,password,dob,total,absent))
   print("sucess")
   con.commit()
   return "sucess"


def getAdmin_values(first_Name):
   con=sqlite3.connect("student_data_base.db")
   cur=con.cursor()
   cur.execute("SELECT * FROM customer WHERE first_name=?", (first_Name,))
   result=cur.fetchall()
   print(result)
   return result
   con.commit()
   print('all good')


def getAdmin_values_employee(first_Name,passwordS):
   con=sqlite3.connect("student_data_base.db")
   cur=con.cursor()
   cur.execute("SELECT * FROM Employee WHERE first_name=? and password=?", (first_Name,passwordS))
   result=cur.fetchall()
   print(result)
   return result
   con.commit()

def getAdmin_values_employee_salary(first_Name,month):
   con=sqlite3.connect("student_data_base.db")
   cur=con.cursor()
   cur.execute("SELECT * FROM Employee WHERE first_name=? and DateOfBirth=?", (first_Name,month))
   result=cur.fetchall()
   print(result)
   return result
   con.commit()   

app = Flask(__name__)

@app.route('/')
def home_html():
   return render_template('index.html')




@app.route('/addAdmin.html')
def addAdmin_html():
   return render_template('addAdmin.html')

@app.route('/add',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      firstname = request.form['uname']
      password = request.form['password']
      mobile=request.form['mobileNumber']
      email=request.form['email']
      print(firstname)
      print(password)
      print(mobile)
      print(email)
      insert_values_to_data_base(firstname,password,mobile,email)
      print("add Sucess")
      return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def admin_login():
   if request.method == 'POST':
      firstname = request.form['uname']
      password = request.form['password']
      print(firstname)
      print(password)
      answer=getAdmin_values(firstname)
      UserName=answer[0][0]
      Password=answer[0][1]
      MobileNmber=answer[0][2]
      Email=answer[0][3]
      if(firstname==UserName and password==Password):
         return render_template('thankyou.html' ,name=UserName,email=Email,mno=MobileNmber)   
      else:
         return 'Invalid User NAme Or Password!'
    
@app.route('/addEmployee.html')
def addEmployee_html():
   return render_template('addEmployee.html')

@app.route('/index.html')
def logout_html():
   return render_template('index.html')   

@app.route('/addemployee',methods = ['POST', 'GET'])
def employee_details():
   if request.method == 'POST':
      firstname = request.form['uname']
      password = request.form['password']
      mobile=request.form['mobileNumber']
      email=request.form['email']
      dateOfBirth=request.form['dob']
      total=request.form['total']
      absent=request.form['absent']
      print(firstname)
      print(password)
      print(mobile)
      print(email)
      print(dateOfBirth)
      print(total)
      print(absent)
      if insert_values_to_data_base_Employee(firstname,password,mobile,email,dateOfBirth,total,absent)=="sucess":
         return render_template('addEmployee.html',report="Sucess")
      else:
         return render_template('addEmployee.html',report="Error")  

@app.route('/employeelogin.html')
def employee_html():
   return render_template('employeelogin.html')


@app.route('/elogin',methods = ['POST', 'GET'])
def employee_login():
   if request.method == 'POST':
      firstname = request.form['uname']
      password = request.form['password']
      print(firstname)
      print(password)
      answer=getAdmin_values_employee(firstname,password)
      ename=answer[0][0]
      emobil=answer[0][0]
      eemail=answer[0][1]
      dateofbirth=answer[0][2]
      nname=ename
      global name
      name=nname
      print(nname)
      return render_template('employee.html',name=nname,mno=emobil,email=eemail,dob=dateofbirth)

@app.route('/salarymonth',methods = ['POST', 'GET'])
def employee_login_salary():
   if request.method == 'POST':
      month=request.form['dob']
      result=getAdmin_values_employee_salary(name,month)
      print(month)
      print(result)
      
      nname=result[0][0]
      emobil=result[0][2]
      eemail=result[0][3]
      dateofbirth=result[0][4]
      global mon
      month=dateofbirth
      mon=month
      total=result[0][5]
      absent=result[0][6]
      present=total-absent
      pf=1000
      mi=1000
      basi=present*2000
      epf=1000
      emi=1000
      eit=0
      if basi>4000:
         eit=2500
      else:
         eit=1000
      netpay=basi-pf-eit-mi     
      print(f'{total} ...')
      print(f'{absent} ...')
      return render_template('employee.html',name=nname,mno=emobil,email=eemail,dob=dateofbirth,no=total,ab=absent,pres=present,basic=basi,pf=epf,it=eit,mi=emi,pay=netpay)


@app.route('/downlord-files/')
def return_files_tut():
   result=getAdmin_values_employee_salary(name,mon)
   nname=result[0][0]
   emobil=result[0][2]
   eemail=result[0][3]
   dateofbirth=result[0][4]
   total=result[0][5]
   absent=result[0][6]
   present=total-absent
   pf=1000
   mi=1000
   basi=present*2000
   epf=1000
   emi=1000
   eit=0
   if basi>4000:
      eit=2500
   else:
      eit=1000
   netpay=basi-pf-eit-mi
   fileName=f"{name}{mon}.pdf"
   pdf=canvas.Canvas(fileName)
   pdf.setTitle(name)
   pdf.drawString(90,791,f"Name:{name}")
   pdf.drawString(375,791,f"Month:{mon}")
   pdf.drawString(20,750,f'Total Working Days:{total}')
   pdf.drawString(220,750,f'Present {present}')
   pdf.drawString(400,750,f'Absent {absent}')
   pdf.drawString(200,680,f"Total-Salary:{basi}")
   pdf.drawString(200,660,f'....Salary deductions....')
   pdf.drawString(200,640,f"Income-Tax:{eit}")
   pdf.drawString(200,620,f"Medical-Insurance :{mi}")
   pdf.drawString(200,600,f"PF:{pf}")
   pdf.drawString(200,580,f'TakeHome......')
   pdf.drawString(200,550,f'Net-Pay:{netpay}')
   pdf.drawString(30,440,f'Sign of HR')
   pdf.drawString(450,440 ,f'Sign of CEO')
   pdf.save()
   return send_file(rf'C:\Users\bittu\OneDrive\Desktop\WebServer\{fileName}', attachment_filename=fileName)


       

if __name__ == '__main__':
   app.run()

