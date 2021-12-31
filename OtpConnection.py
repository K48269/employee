
import smtplib
import random

class OtpConnection:
    def SendEmail(self,email,otp):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('bittukiran123@gmail.com','tphggvuxeqaylhru')
        server.sendmail('bittukiran123@gmail.com',email,otp)
        print('Mail Sent')
        return True


    def generateOTP(self):
        digits = ["1","2","3","4","5","6","7","8","9","0"]
        OTP = ""
        for i in range(4) :
            OTP += random.choice(digits)
        return OTP




a=OtpConnection()