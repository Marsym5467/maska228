import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('top://5.tcp.eu.ngrok.io', 14467))

msg = input("Введіть повідомлення:")
client_socket.send('Привіт сервер!'.encode())

response = client_socket.recv(1024).decode()

print(f'Відповідь від сервера: {response}')

client_socket.close()