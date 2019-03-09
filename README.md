# secureChat
#### client and server that use RSA and AES to communicate securely
## Usage:
1. Ensure client.py and server.py have the same host and port (by default localhost port 5022)
2. Run server.py with 'python3 server.py' command
3. Run client.py with 'python3 server.py' command

## How it works:
1. The server creates an RSA public and private key (using the .pem file generated with Keytool)
2. The client connects to the server
3. The server sends it's public key to the client
4. The client creates an AES key and encrypts it with the RSA public key it received from the server
5. The client sends this encrypted AES key to the server
6. The server decrypts the AES key with its private RSA key
7. All future messages are encrypted and decrypted using the AES key

## Note:
- Only the server.py needs access to the mykey.pem file.  
- A different .pem file could and should be used to replace mykey.pem in actual use.  
- The AES key should be changed from 'zebrabluestripes'.

