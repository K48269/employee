from os import name
from DBConnection import DB
from EncryptionAndDrycption import EncryptionAndDecryption
from flask import Flask,render_template,request
from OtpConnection import OtpConnection


db=DB()
ed=EncryptionAndDecryption()
otP=OtpConnection()


app = Flask(__name__)




#login Page
@app.route("/")
def login_page():
    print('loginPage')
    return render_template('login.html')


#login Check
@app.route('/add',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      id = request.form['id']
      password= request.form['password']
      global check 
      check = db.select_values(id)
      if(len(check)==0):
          return render_template('login.html',status="Invalid User-Name")
      else:
          id_check=check[0][0]
          key=check[0][4].encode("utf-8")
          e_password=check[0][5].encode("utf-8")
          fetch_password=ed.decrypt_password(e_password,key)
          global otp
          if (id_check==id and fetch_password==password):
              otp=otP.generateOTP()
              user_email=check[0][3]
              otP.SendEmail(user_email,otp)
              return render_template('otp.html',status='Sent successfull')  
          else:
              return render_template('login.html',status="Invalid Password")    



@app.route('/checkotp',methods = ['POST', 'GET'])
def check_otp():
     if request.method == 'POST':
      g_otp = request.form['otp']
      if(otp==g_otp):
          return render_template('user_info.html',uid=check[0][0],name=check[0][1],email=check[0][3],mno=check[0][2])




    

#add Employee page
@app.route("/NewEmployee.html")
def Create_User():
    return render_template('NewEmployee.html')


#add Employee form
@app.route('/addEmployee',methods = ['POST', 'GET'])
def new_User():
    if request.method == 'POST':
      id = request.form['id']
      Name = request.form['name']
      Password=request.form['password']
      no=request.form["mno"]
      email=request.form["email"]
      if (id=='' and Name=='' and Password=='' and no=='' and email==''):
          return render_template('NewEmployee.html')
      else:        
          passw=ed.encrypt_obj(Password)
          db.insert(id,Name,no,email)
          db.login_credentails(id,passw[0],passw[1])
          return render_template("login.html")


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
