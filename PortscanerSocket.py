import socket

ip = input("Digite o ip do alvo: ")

for port in range(65535):
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((ip, port))
        if serv.connect_ex((ip, port)):
            print("Portas abertas:", port)
    finally:
        serv.close()
