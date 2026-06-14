import requests
import ssl
import urllib3
import socket

server_connection_manager  = socket.socket()

port = 6767

server.bind(("",port))
print("socket binded to %s" %(port))

server.listen(50)
print("socket is listening")

while true:

	c, addr = server.accept()

	print("received connection from: ", adrr)

	c.send("Thank you for connecting".encode())

	c.close()

	break
	
