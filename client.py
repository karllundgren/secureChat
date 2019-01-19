import socket
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import threading


class client:
	s=socket.socket()
	host='127.0.0.1'
	sport=5022
	def sendMsg(self):
		while True:
			message=raw_input("\n\nEnter a message: ")
			self.s.send(self.cipher.encrypt(message))

	def __init__(self):
		self.s.connect((self.host,self.sport))
		message=''

		#AES key
		aesKey=b'zebrabluestripes'

		#RSA recieve
		publicRSA=self.s.recv(1024)
		RSAkey=RSA.importKey(publicRSA)

		self.s.send("client has recieved public key")
		print "public key recieved\n"
		
		#AES encryption
		AESencrypted=RSAkey.encrypt(aesKey,3)
		self.s.send(AESencrypted[0])
		print "AES encrypted key sent\n"
		
		#AES object creation
		self.cipher=AES.new(aesKey, AES.MODE_CFB, aesKey)

		#Encrypted communication
		iThread=threading.Thread(target=self.sendMsg)
		iThread.daemon=True
		iThread.start()
		
		while True:
			data=self.s.recv(1024)
			if not data:
				break
			print "\n"+self.cipher.decrypt(data)
	
c=client()
while True:
	c.sendMsg()
