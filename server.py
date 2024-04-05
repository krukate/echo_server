import socket
import logging

logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Словарь для хранения клиентов (IP-адрес : имя)
clients = {}

host = input("Введите имя хоста (по умолчанию 127.0.0.1): ") or '127.0.0.1'
port = int(input("Введите номер порта (по умолчанию 9090): ") or 9090)

sock = socket.socket()
while True:
    try:
        sock.bind((host, port))
        break
    except OSError:
        logging.warning(f"Порт {port} занят, пытаюсь найти доступный порт")
        port += 1

print(f"Сервер запущен на порту: {port}")
logging.info(f"Запуск сервера на порту: {port}")

sock.listen(0)
logging.info("Начало прослушивания")

while True:
    conn, addr = sock.accept()
    logging.info(f"Подключен клиент: {addr}")

    client_ip = addr[0]

    if client_ip in clients:
        conn.send(f"Привет, {clients[client_ip]}! Если хотите выйти, введите 'exit'".encode())
    else:
        conn.send("Добро пожаловать! Пожалуйста, введите свое имя: ".encode())
        data = conn.recv(1024)
        client_name = data.decode()
        clients[client_ip] = client_name
        logging.info(f"Новый клиент добавлен: {client_name}")

    while True:
        data = conn.recv(1024)
        msg = data.decode()
        if msg:
            if msg == "exit":
                logging.info("Клиент запросил отключение")
                conn.close()
                break

            logging.info(f"Данные от клиента получены: {msg}")
            conn.send(data)
            logging.info(f"Данные отправлены клиенту: {msg}")

            # Дополнительно сохраняем обновленный список клиентов в файл
    with open('clients.txt', 'w') as file:
        for ip, name in clients.items():
            file.write(f"{ip}:{name}\n")