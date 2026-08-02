import socket
import threading

host = '127.0.0.1' #localhost

port = 4443

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen(7000)

clients = []
nicks = []

def broadcast(message):

	for client in clients:
		try:
			client.send(message)
		except():
			pass

def handle(client):

	while True:

		try:
			message = client.recv(1024)
			broadcast(message)

		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicks[index]
			broadcast(f"{nickname} left the chat...".encode('ascii'))
			nicks.remove(nickname)
			break

def receive():

	while True:
		
		client,address = server.accept()
		print(f"Connected with {str(address)}")
		client.send("NICK".encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicks.append(nickname)
		clients.append(client)

		print(f"nickname of the client is: {nickname}")
		broadcast(f"{nickname} joined the chat".encode('ascii'))
		client.send("Connected to the server".encode('ascii'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

print("Server is listening...")
receive()