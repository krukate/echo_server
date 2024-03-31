import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
print("Запуск сервера")
sock.listen(0)
print("Начало прослушивания")

while True:
    conn, addr = sock.accept()
    print(f"Подключен клиент: {addr}")

    while True:
        data = conn.recv(1024)
        msg = data.decode()
        if msg == "exit":
            print("Клиент запросил отключение")
            conn.close()
            break

        print(f"Данные от клиента получены: {msg}")
        conn.send(data)
        print(f"Данные отправлены клиенту: {msg}")

#print("Остановка сервера")
#sock.close()