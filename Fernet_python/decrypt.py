import os
from cryptography.fernet import Fernet
#Disclaimer: For educational use  only
files = []
for file in os.listdir():
	if file == "encrypt.py" or file== "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
key=Fernet.generate_key()
with open ("thekey.key","rb") as key:
	secretkey= key.read()
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
print("You have successfully decrypted your files")
print("\n This has been made for educational purposes only by WhiteHatCyberus")
print("\n Cyberus does not entertain malicious use of its applications")
