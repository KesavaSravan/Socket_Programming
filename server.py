# import the socket library
import socket           

#Create a socket object
s = socket.socket()     
print ("Socket object successfully created")


HOST = "192.168.91.1" 
PORT = 65000  # Port to listen   

# Bind to the port
s.bind((HOST,PORT))      
print ("socket binded to %s" %(PORT))

# Socket in listening mode
s.listen() 
print ("socket is listening")       

#Write your application code here
while True:

# Establish connection with client.
    c, addr = s.accept()    
    print ('Got connection from', addr )

    c.sendall(b'Thank you for connecting')
    data=c.recv(1024)
    print ("message from client:",data)
# Close the connection with the client
    c.close()
