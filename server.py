import socket
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import threading

class client:
	host='127.0.0.1'
	sport=5022
	def sendMsg(self):
		while True:
			message=raw_input("\n\nEnter a message: ")
			self.c.send(self.cipher.encrypt(message))

	def __init__(self):
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,self.sport))
		self.sock.listen(1)
		self.c,self.a=self.sock.accept()

		#RSA import
		f=open('mykey.pem','r')
		key=RSA.importKey(f.read())
		print "RSA key imported\n"
		
		#RSA export and send public key
		publicRSAkey=key.publickey().exportKey('DER')
		self.c.send(publicRSAkey)
		print "Public RSA key sent\nmessage from client: "+self.c.recv(1024)+"\n"
		
		#AES recieve and decrypt
		AESencrypted=self.c.recv(1024)
		#print "\n"+AESencrypted+"\n"
		aesKey=key.decrypt(AESencrypted)
		print "AES encrypted key recieved and decrypted"
		
		#AES object creation
		self.cipher=AES.new(aesKey, AES.MODE_CFB, aesKey)
		
		#Encrypted communication
		iThread=threading.Thread(target=self.sendMsg)
		iThread.daemon=True
		iThread.start()
		
		while True:
			data=self.c.recv(1024)
			if not data:
				break
			print (self.cipher.decrypt(data))

cl=client()
while True:
	cl.sendMsg()
