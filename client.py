import time, socket, sys
print("\nWelcome to Chat Room\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
print(shost)
ip = socket.gethostbyname(shost)
print(ip)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nConnecting to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("MSG : "))
    s.send(message.encode())