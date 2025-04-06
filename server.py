import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 14467))

server_socket.listen(1)
print(f'Сервер очікує підключення')

connection, address = server_socket.accept()
print(f'Підключився клієнт: {address}')

data = connection.recv(1824).decode()
print(f'Отримано повідомлення від клієнта: {data}')

if data == "INFO":
    connection.send('Це чат від логіки!!'.encode())
elif data == "HELP":
    connection.send('Доступні команди: HELP, INFO'.encode())
else:
    connection.send('Невідома команда'.encode())

connection.close()
server_socket.close()