'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Checkpoint 2 - 2° Semestre
Alunos:
João Paulo Silva de Queiroz - RM86376
Mateus Amado Monteiro da Silva - RM87974
'''

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
