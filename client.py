import socket

host = input("Введите имя хоста (по умолчанию 127.0.0.1): ") or '127.0.0.1'
port = int(input("Введите номер порта (по умолчанию 9090): ") or 9090)

sock = socket.socket()
sock.connect((host, port))
print("Подключение к серверу")

first_connection = True

while True:
    if first_connection:
        response = sock.recv(1024).decode()
        print(response)
        if "Пожалуйста, введите свое имя" in response:
            name = input("Введите ваше имя: ")
            sock.send(name.encode())
            first_connection = False
        else:
            first_connection = False

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