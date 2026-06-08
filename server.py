import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

print("Waiting for connection...")

client, address = s.accept()

print("Connected to:", address)

while True:

    message = input("Server: ")
    client.send(message.encode('utf-8'))

    if message.lower() == "bye":
        break

    client_message = client.recv(1024).decode('utf-8')
    print("Client:", client_message)

    if client_message.lower() == "bye":
        break

client.close()
s.close()

print("Connection Closed")