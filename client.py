import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
print("Подключение к серверу")

while True:

    msg = input("Введите сообщение для отправки: ")

    if msg == "exit":
        sock.send(msg.encode())
        sock.close()
        print("Отключение от сервера")
        break

    sock.send(msg.encode())
    print(f"Данные отправлены на сервер: {msg}")

    data = sock.recv(1024)
    print(f"Данные от сервера получены: {data.decode()}")
