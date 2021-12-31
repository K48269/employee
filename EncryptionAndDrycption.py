from cryptography.fernet import Fernet

class EncryptionAndDecryption:
    def encrypt_obj(self,message):
        key=Fernet.generate_key()
        msg_encrypt=message.encode()
        f_obj=Fernet(key)
        a=f_obj.encrypt(msg_encrypt)
        return a,key

    def decrypt_password(self,key_1,encrypt_date):
        key=key_1
        f_obj=Fernet(key)
        b=f_obj.decrypt(encrypt_date).decode("utf-8")
        return b





