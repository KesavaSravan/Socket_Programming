# Import socket module
import socket           
# Create a socket object
s = socket.socket()     
HOST = "192.168.91.64"  
PORT = 65000  
# connect to the server on local computer
s.connect((HOST,PORT))
# receive data from the server and decoding to get the string.
data=s.recv(1024)
print ("message from server:",data)
s.sendall(b"This is a hello from client 1")
# close the connection
s.close()   
    
