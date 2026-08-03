import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('0.tcp.in.ngrok.io', 29893))

nickname = input("Enter Your Nickname(You Will Identified By This In The Room): ")

def receive():

	while True:

		try:
			message = client.recv(1024).decode('ascii')
			if message == "NICK":
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		
		except:
			print("An Error has occurred... Closing connection...")
			client.close()
			break
	
def write():

	while True:
		message = f"{nickname}: {input('')}"
		client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()