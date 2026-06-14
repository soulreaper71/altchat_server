import requests
import urllib3
import socket

server_connection_manager  = socket.socket()

port = 6767

server_connection_manager.bind(("",port))
print("socket binded to %s" %(port))

server_connection_manager.listen(50)
print("socket is listening")

while True:

	c, addr = server_connection_manager.accept()

	print("received connection from: ", adrr)

	c.send("You are currently connected to altchat messaging service... Thank You for connecting... your".encode())
	c.send("Your connection was terminated...".encode())
	c.close()

	break
	
