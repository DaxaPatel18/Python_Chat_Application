import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

while True:

    server_message = s.recv(1024).decode('utf-8')
    print("Server:", server_message)

    if server_message.lower() == "bye":
        break

    message = input("Client: ")
    s.send(message.encode('utf-8'))

    if message.lower() == "bye":
        break

s.close()

print("Connection Closed")