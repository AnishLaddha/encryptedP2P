from cryptography.fernet import Fernet
import hashlib
import os.path
from os import path

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key","rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def main():
    usrfile = str(input("file name: "))
    usrcrypt = int(input("type 0 for encryption and 1 for decryption: "))
    if(path.exists("key.key")==False):
        write_key()
    key = load_key()
    if(usrcrypt == 0):
        encrypt(usrfile,key)
    else:
        decrypt(usrfile,key)
if __name__ == "__main__":
    main()
