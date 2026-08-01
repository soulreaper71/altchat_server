import socket

class connection_handler: 

	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def __init__(self):
		pass

	def connect():
		
		tcp_socket.bind('',443)
		tcp_socket.listen(7000)
		
		while 1: 
			client,addr = tcp_socket.accept()
			client.send("Hello. Brave Traveller.", )
			client.send("We will terminate this connection now.")
