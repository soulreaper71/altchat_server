import socket

class connection_handler: 

	
	def __init__(self):
		pass

	def connect():

		tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
		tcp_socket.bind(('',443))
		tcp_socket.listen(7000)
		print ("socket is listening")
		
		while 1: 
			client,addr = tcp_socket.accept()
			print ('Got connection from', addr )
			client.send("Hello. Brave Traveller.".encode() )
			client.send("We will terminate this connection now.".encode())

