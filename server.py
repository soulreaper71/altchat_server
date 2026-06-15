import requests
import urllib3
import socket

server_connection_manager  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 6971

server_connection_manager.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_connection_manager.bind(("",port))
print("socket binded to %s" %(port))

server_connection_manager.listen(50)
print("socket is listening")

while True:
	c, addr = server_connection_manager.accept()
	if addr == "127.0.0.1":
		c.close()
	else:
		print("received connection from: ", addr)
		c.send("You are currently connected to altchat messaging service... Thank You for connecting... your".encode())
		c.send("Your connection was terminated...".encode())
		c.close()
		
